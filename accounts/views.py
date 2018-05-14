from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from accounts.models import BaseInfoUser
from blogger.models import BloggerProfile
from .forms import BaseUserInfoForm, UserForm
#it used to be DonatorProfileForm so check it if it has a differenc content in previous that migh create  issue.

def settings(request):

    return render(request,'accounts/settings.html')
    pass
def razoweblogshuby(request):

    return render(request,'accounts/razoweblogshuby.html',)

#CHECK THIS ONE OUT..
def quick_register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        bf = BaseUserInfoForm(request.POST)
        print(request.POST)
        print('uf.is_valid()-->',uf.is_valid(),'bf.is_valid()-->',bf.is_valid())
        if uf.is_valid() and bf.is_valid():
            user = uf.save()
            baseinfo_obj = BaseInfoUser.objects.get(user=user)
            baseinfo_obj.nature = bf.cleaned_data['nature']
            baseinfo_obj.save()
            print('baseinfo_obj.nature-->', baseinfo_obj.nature)
            if baseinfo_obj.nature == 'Blogger':
                print('user-->',user)
                profile, create = BloggerProfile.objects.get_or_create(user=user,pk=request.user.pk)
                if create is True:
                    profile.name = uf.cleaned_data['first_name'] + uf.cleaned_data['last_name']
                    profile.email = uf.cleaned_data['email']
                    profile.save()
                print('profile.name-->', profile.name)
        return redirect('/posts/')
    else:
        uf = UserForm()
        bf = BaseUserInfoForm(request.POST)
        return render(request, 'accounts/reg_form.html', {'user_form': uf,'baseinfo_form':bf})






def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
        return redirect(reverse(viewname='posts:list'))
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request,'accounts/change_password.html',{'form':form})
