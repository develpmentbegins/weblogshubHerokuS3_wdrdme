from django.shortcuts import redirect, render


def login_redirect(request):
    return redirect('/account/login')

def home(request):
    return render(request, template_name='home.html')

