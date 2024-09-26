from . import views
from django.urls import path


urlpatterns = [
    path('', views.get_all_blogs, name='get_all_blogs'),
    path('search', views.search_blogs, name='search_blog'),
    path('posted-in-last-month', views.get_blogs_posted_within_last_month, name='blogs_within_last_month'),
    path('posted-in-last-3-months', views.get_blogs_posted_within_last_3_months, name='blogs_within_last_3_months'),
    path('posted-in-last-6-months', views.get_blogs_posted_within_last_6_months, name='blogs_within_last_6_months'),
    path('posted-in-last-year', views.get_blogs_posted_within_last_year, name='blogs_within_last_year'),
    path('create', views.create_blog, name='create_blog'),
    path('<str:blog_id>', views.get_specific_blog, name='get_blog'),
    path('user/<str:uid>', views.get_all_user_blogs, name='get_all_user_blogs'),
    path('<str:blog_id>/update', views.update_blog, name='update_blog'),
    path('<str:blog_id>/delete', views.delete_blog, name='delete_blog'),
]