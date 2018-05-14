from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import BloggerProfile
from .forms import BloggerProfileForm

def blogger_profile(request):
    print('request.user.bloggerprofile.pk-->',request.user.bloggerprofile.pk)
    blogger_profile = BloggerProfile.objects.get(pk=request.user.bloggerprofile.pk)
    print(blogger_profile)
    context = {'object': blogger_profile,'user':request.user}
    return render(request, template_name='blogger/blogger_myprofile.html',context=context)



class BloggerProfileListView(ListView):
    model = BloggerProfile


class BloggerProfileCreateView(CreateView):
    model = BloggerProfile
    form_class = BloggerProfileForm


class BloggerProfileDetailView(DetailView):
    model = BloggerProfile


class BloggerProfileUpdateView(UpdateView):
    model = BloggerProfile
    form_class = BloggerProfileForm

