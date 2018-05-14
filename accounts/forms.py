from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


#
# class Register_NowForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username','email',]
from accounts.models import BaseInfoUser
# from donator.models import BloggerProfile


class UserForm(forms.ModelForm):
    # password = forms.PasswordInput()
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)

class BaseUserInfoForm(forms.ModelForm):
    class Meta:
        model = BaseInfoUser
        fields = ('nature',)


