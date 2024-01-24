from . import views
from django.urls import path


urlpatterns = [
    path('<str:blog_id>/add', views.add_comment_view, name='add_comment'),
    path('<uuid:comment_id>', views.get_specific_comment_view, name='get_specific_comment'),
    path('blog/<str:blog_id>', views.get_comments_on_blog_view, name='get_comments_on_blog'),
    path('user/<str:uid>', views.get_comments_by_user_view, name='get_comments_by_user'),
    path('<uuid:comment_id>/delete', views.delete_comment_view, name='delete_comment'),
]