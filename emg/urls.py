"""emg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from main import views
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'login/$', views.login_view, name='login_view'),
    url(r'logout/$', views.logout_view, name='logout_view'),
    url(r'mybids/$', views.mybids, name='mybids'),
    url(r'myitems/$', views.myitems, name='myitems'),
    url(r'add_item/$', views.add_item, name='add_item'),
    url(r'delete_item/(?P<id>\d*)/$', views.delete_item, name='delete_item'),
    url(r'item/(?P<id>\d*)/$', views.item, name='item'),
    url(r'search/$', views.search, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)