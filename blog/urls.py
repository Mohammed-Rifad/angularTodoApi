from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog_list', views.blog_list, name='blog-list'),
    path('blog_detail/<int:pk>', views.blog_detail, name='blog-detail'),
    path('create/',views. create_blog, name='blog-create'),
    path('update/<int:pk>', views.update_blog, name='blog-update'),
    path('delete/<int:pk>', views.delete_blog, name='blog-delete'),
    path('approve/<int:pk>', views.approve_blog, name='blog-approve'),
    path('reject/<int:pk>', views.reject_blog, name='blog-reject'),
    path('like/<int:blog_id>/<int:user>', views.like_blog, name='like-blog'),
    path('user_blog/<int:user>', views.view_user_blogs, name='user-blog'),
]