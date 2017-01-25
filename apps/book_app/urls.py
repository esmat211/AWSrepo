from django.conf.urls import url
# from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    url(r'^create_author$', views.create_author),
    url(r'^create_book$', views.create_book),
]
