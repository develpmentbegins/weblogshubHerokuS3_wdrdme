from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

NATURE_CHOICES = (
    ('Blogger', 'Blogger'),
)

class BaseInfoUser(models.Model):
    user = models.OneToOneField(User)
    # profile_id = models.SlugField(unique=True,)
    nature = models.CharField(max_length=20, choices=NATURE_CHOICES,default='Blogger')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        # self.item_id = uniqueCodeGenerator()
        # print('Base info jst got created and profile_id is ',self.profile_id)
        super(BaseInfoUser, self).save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_baseinfouser(sender, instance, created, **kwargs):
    if created:
        BaseInfoUser.objects.create(user=instance, pk=instance.pk)



# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from utilities import uniqueCodeGenerator
#
#
# NATURE_CHOICES = (
#     ('OFFICER', 'OFFICER'),
#     ('RECEIVER', 'RECEIVER'),
#     ('VOLUNTEER', 'VOLUNTEER'),
# )
#
# class BaseInfoUser(models.Model):
#     user = models.OneToOneField(User)
#     # profile_id = models.SlugField(unique=True,)
#     nature = models.CharField(max_length=20, choices=NATURE_CHOICES,null=True,blank=True)
#
#     def __str__(self):
#         return self.user.username
#
#     def save(self, *args, **kwargs):
#         self.item_id = uniqueCodeGenerator()
#         # print('Base info jst got created and profile_id is ',self.profile_id)
#         super(BaseInfoUser, self).save(*args, **kwargs)
#
#
# @receiver(post_save, sender=User)
# def create_baseinfouser(sender, instance, created, **kwargs):
#     if created:
#         BaseInfoUser.objects.create(user=instance, pk=instance.pk)
#
