from django.conf.urls import url
from accounts import views

from django.contrib.auth.views import (
    login,
    logout,
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
    )

urlpatterns = [
    url(r'^login/$', login, {'template_name':'accounts/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name':'accounts/logout.html'}, name='logout'),
    url(r'^quick_register/$', views.quick_register, name='quick_register'),
    url(r'^razoweblogshuby/$', views.razoweblogshuby, name='razoweblogshuby'),

    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^reset_password/$', password_reset, {'template_name': 'accounts/reset_password.html','email_template_name':'accounts/reset_password_email.html', 'post_reset_redirect':'accounts:password_reset_done'}, name='reset_password'),
    url(r'^reset_password/done/$', password_reset_done, {'template_name': 'accounts/reset_password_done.html'}, name='password_reset_done'),
    url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
    password_reset_confirm,{'post_reset_redirect':'accounts:password_reset_complete', 'template_name':'accounts/reset_password_complete.html'},name='password_reset_confirm'),
    url(r'^reset_password/complete/$', password_reset_complete,{'template_name':'accounts/reset_password_confirm.html'}, name='password_reset_complete'),
    url(r'^settings$', views.settings, name='settings'),
]