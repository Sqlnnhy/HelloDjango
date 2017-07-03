"""HelloDjango URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from myapp import views as myapp_views

urlpatterns = [
    url(r'^index', myapp_views.index),
    url(r'^rss', myapp_views.rss_view),
    url(r'^boot', myapp_views.boot_view),
    url(r'^add_view', myapp_views.add_view, name='add'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^quickstart/', include('quickstart.urls', namespace="quickstart")),
    url(r'^admin/', include(admin.site.urls)),
]
