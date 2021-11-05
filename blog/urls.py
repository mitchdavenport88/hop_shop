from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_posts, name='blog_posts'),
    path('<slug>/', views.blog_detail, name='blog_detail'),
]
