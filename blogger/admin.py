from django.contrib import admin
from django import forms
from .models import BloggerProfile

class BloggerProfileAdminForm(forms.ModelForm):

    class Meta:
        model = BloggerProfile
        fields = '__all__'


class BloggerProfileAdmin(admin.ModelAdmin):
    form = BloggerProfileAdminForm
    list_display = ['name', 'blogger_id', 'email', 'phone', 'city', 'state', 'pin', 'image', 'claps', 'birthdate', 'bio', 'created', 'portfolio', 'journ_with_us', 'business_rate', 'net_business']
    # readonly_fields = ['name', 'blogger_id', 'email', 'phone', 'city', 'state', 'pin', 'image', 'claps', 'birthdate', 'bio', 'created', 'portfolio', 'journ_with_us', 'business_rate', 'net_business']

admin.site.register(BloggerProfile, BloggerProfileAdmin)


