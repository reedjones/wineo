__author__ = 'reed'


from django.conf.urls import url
from .views import user_profile, my_profile


urlpatterns = [
     url(r'^(?P<profile_id>[0-9]+)/$', user_profile, name='user-profile'),
     url(r'^my_profile/$', my_profile, name='my-profile'),
]