__author__ = 'reed'
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^register/$', views.register, name="register"),
    url(r'^photo/$', views.add_photo, name="add_photo"),
    url(r'^login/$', views.login_, name="login"),
    url(r'^logout/$', views.logout_, name="logout"),

]