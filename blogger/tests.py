import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import BloggerProfile
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_bloggerprofile(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["blogger_id"] = "blogger_id"
    defaults["email"] = "email"
    defaults["phone"] = "phone"
    defaults["city"] = "city"
    defaults["state"] = "state"
    defaults["pin"] = "pin"
    defaults["image"] = "image"
    defaults["claps"] = "claps"
    defaults["birthdate"] = "birthdate"
    defaults["bio"] = "bio"
    defaults["portfolio"] = "portfolio"
    defaults["journ_with_us"] = "journ_with_us"
    defaults["business_rate"] = "business_rate"
    defaults["net_business"] = "net_business"
    defaults.update(**kwargs)
    if "user" not in defaults:
        defaults["user"] = create_user()
    return BloggerProfile.objects.create(**defaults)


class BloggerProfileViewTest(unittest.TestCase):
    '''
    Tests for BloggerProfile
    '''
    def setUp(self):
        self.client = Client()

    def test_list_bloggerprofile(self):
        url = reverse('blogger_bloggerprofile_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_bloggerprofile(self):
        url = reverse('blogger_bloggerprofile_create')
        data = {
            "name": "name",
            "blogger_id": "blogger_id",
            "email": "email",
            "phone": "phone",
            "city": "city",
            "state": "state",
            "pin": "pin",
            "image": "image",
            "claps": "claps",
            "birthdate": "birthdate",
            "bio": "bio",
            "portfolio": "portfolio",
            "journ_with_us": "journ_with_us",
            "business_rate": "business_rate",
            "net_business": "net_business",
            "user": create_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_bloggerprofile(self):
        bloggerprofile = create_bloggerprofile()
        url = reverse('blogger_bloggerprofile_detail', args=[bloggerprofile.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_bloggerprofile(self):
        bloggerprofile = create_bloggerprofile()
        data = {
            "name": "name",
            "blogger_id": "blogger_id",
            "email": "email",
            "phone": "phone",
            "city": "city",
            "state": "state",
            "pin": "pin",
            "image": "image",
            "claps": "claps",
            "birthdate": "birthdate",
            "bio": "bio",
            "portfolio": "portfolio",
            "journ_with_us": "journ_with_us",
            "business_rate": "business_rate",
            "net_business": "net_business",
            "user": create_user().pk,
        }
        url = reverse('blogger:blogger_bloggerprofile_update', args=[bloggerprofile.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


