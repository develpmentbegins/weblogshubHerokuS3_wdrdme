from django import forms
from .models import BloggerProfile


class BloggerProfileForm(forms.ModelForm):
    class Meta:
        model = BloggerProfile
        fields = ['name', 'blogger_id', 'email', 'phone', 'city', 'state', 'pin', 'image', 'claps', 'birthdate', 'bio', 'portfolio', 'journ_with_us', 'business_rate', 'net_business', 'user']


