from . import views
from django.urls import path


urlpatterns = [
    path('', views.get_all_blogs_view, name='get_all_blogs'),
    path('create', views.create_blog_view, name='created_blog'),
    path('<str:blog_id>', views.get_specific_blog_view, name='get_blog'),
    path('user/<str:uid>', views.get_all_user_blogs_view, name='get_all_user_blogs'),
    path('<str:blog_id>/update', views.update_blog_view, name='update_blog'),
    path('<str:blog_id>/delete', views.delete_blog_view, name='delete_blog'),
]