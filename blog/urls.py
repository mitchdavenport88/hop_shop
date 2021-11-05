from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_posts, name='blog_posts'),
]
