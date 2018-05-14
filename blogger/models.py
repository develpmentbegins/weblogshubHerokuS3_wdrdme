from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class BloggerProfile(models.Model):

    # Fields
    name = CharField(max_length=100,null=True,blank=True)
    blogger_id = SlugField(null=True,blank=True)
    email = EmailField()
    phone = CharField(max_length=100,null=True,blank=True)
    city = CharField(max_length=100,null=True,blank=True)
    state = CharField(max_length=100,null=True,blank=True)
    pin = IntegerField(null=True,blank=True)
    image = ImageField(null=True,blank=True)
    claps = IntegerField(null=True,blank=True)
    birthdate = DateField(null=True,blank=True)
    bio = CharField(max_length=500, null=True,blank=True)
    created = DateField(auto_now_add=True)
    portfolio = URLField(null=True,blank=True)
    journ_with_us = URLField(null=True,blank=True)
    business_rate = CharField(max_length=100,null=True,blank=True)
    net_business = CharField(max_length=100,null=True,blank=True)

    # Relationship Fields
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('blogger:blogger_bloggerprofile_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('blogger:blogger_bloggerprofile_update', args=(self.pk,))


