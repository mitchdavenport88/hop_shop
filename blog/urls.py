from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_posts, name='blog_posts'),
    path('add_post/', views.add_blog_post, name='add_blog_post'),
    path('edit_post/<slug:slug>/', views.edit_blog_post,
         name='edit_blog_post'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
]
