"""WineO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from wines import views as wine
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', wine.wine_index, name='wine-index'),
     url(r'^accounts/', include('accounts.urls')),
      url(r'^profiles/', include('profiles.urls')),

    url(r'^wine/add/$', wine.add_wine, name='add-wine'),

    url(r'^wine/(?P<pk>[0-9]+)/$', wine.wine_single, name='wine-index'),

    url(r'^wine/(?P<pk>[0-9]+)/write_note/$', wine.write_note, name='write-note'),

    url(r'^wine/(?P<pk>[0-9]+)/delete/$', wine.delete_wine, name='delete-wine'),

    url(r'^wine/(?P<pk>[0-9]+)/edit/$', wine.edit_wine, name='edit-wine'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
