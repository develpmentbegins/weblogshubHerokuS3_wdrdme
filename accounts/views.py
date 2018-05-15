from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from accounts.models import BaseInfoUser
from blogger.models import BloggerProfile
from weblogshub.settings import EMAIL_HOST_USER
from .forms import BaseUserInfoForm, UserForm
#it used to be DonatorProfileForm so check it if it has a differenc content in previous that migh create  issue.
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import CustomUserCreationForm

#...
def signup(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            username = f.cleaned_data['username']
            raw_password = f.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            profile, create = BloggerProfile.objects.get_or_create(user=request.user, pk=request.user.pk)
            if create is True:
                profile.email = f.cleaned_data['email']
                profile.save()
            print('profile.name-->', profile.name)
        else:
            messages.info(request,"Something went wrong please fill out the details once more. THank you!")
            return redirect(reverse('accounts:signup'))
            # send_mail(subject, message, from_email, to_list, fail_silently=True)
        subject = 'We thank you for signing up'
        message = 'YOu have successfully signed up!./n Thank you for joining us!./n YOu will get an email to setup your password very very soon...'
        from_email = EMAIL_HOST_USER
        to_list = [f.cleaned_data['email'], 'deepaksingh.18feb@gmail.com', ]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        print('email is just sent')
        return redirect('/posts/')
    else:
        f = CustomUserCreationForm()

    return render(request, 'accounts/signup.html', {'form': f})

def settings(request):

    return render(request,'accounts/settings.html')
    pass


def razoweblogshuby(request):

    return render(request,'accounts/razoweblogshuby.html',)

#CHECK THIS ONE OUT..
def quick_register(request):
    if request.method == 'POST':
        uf = UserCreationForm(request.POST)
        bf = BaseUserInfoForm(request.POST)
        print(request.POST)
        print('uf.is_valid()-->',uf.is_valid(),'bf.is_valid()-->',bf.is_valid())
        if uf.is_valid() and bf.is_valid():
            # username = uf.cleaned_data.get('username')
            # raw_password = uf.cleaned_data.get('password')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
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
        #send_mail(subject, message, from_email, to_list, fail_silently=True)
        subject = 'We thank you for signing up'
        message = 'YOu have successfully signed up!./n Thank you for joining us!./n YOu will get an email to setup your password very very soon...'
        from_email = EMAIL_HOST_USER
        to_list = [uf.cleaned_data['email'],'deepaksingh.18feb@gmail.com',]
        send_mail(subject,message,from_email,to_list,fail_silently=True)
        print('email is just sent')
        return redirect('/posts/')
    else:
        uf = UserCreationForm()
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
