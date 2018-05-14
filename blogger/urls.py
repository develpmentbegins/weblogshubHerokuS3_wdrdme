from django.conf.urls import url, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'bloggerprofile', api.BloggerProfileViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    url(r'^myprofile/$', views.blogger_profile, name='blogger_profile'),
    # urls for BloggerProfile
    url(r'^bloggerprofile/$', views.BloggerProfileListView.as_view(), name='blogger_bloggerprofile_list'),
    url(r'^bloggerprofile/create/$', views.BloggerProfileCreateView.as_view(), name='blogger_bloggerprofile_create'),
    url(r'^bloggerprofile/detail/(?P<pk>\S+)/$', views.BloggerProfileDetailView.as_view(), name='blogger_bloggerprofile_detail'),
    url(r'^bloggerprofile/update/(?P<pk>\S+)/$', views.BloggerProfileUpdateView.as_view(), name='blogger_bloggerprofile_update'),
)

