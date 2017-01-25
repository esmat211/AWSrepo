from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^create$', views.create, name = 'create'),
    url(r'^book_to_publisher$', views.book_to_publisher, name = 'book_to_publisher'),
]
