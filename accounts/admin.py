from django.contrib import admin
from .models import BaseInfoUser

# Register your models here.
#
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('user','profile_id', 'user_info', 'address', 'phone', 'website')
#
#     def user_info(self, obj):
#         print(self)
#         print(obj)
#         return obj.description
#     user_info.short_description = 'info'
#
#     def get_queryset(self, request):
#         queryset = super(UserProfileAdmin, self).get_queryset(request)
#         queryset = queryset.order_by('-phone', 'user')
#         return queryset


admin.site.register(BaseInfoUser)

