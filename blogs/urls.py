from . import views
from django.urls import path


urlpatterns = [
    path('', views.get_all_blogs_view, name='get_all_blogs'),
    path('search', views.search_blogs_view, name='search_blog'),
    path('within-last-month', views.get_blogs_posted_within_last_month_view, name='blogs_within_last_month'),
    path('within-last-3-months', views.get_blogs_posted_within_last_3_months_view, name='blogs_within_last_3_months'),
    path('within-last-6-months', views.get_blogs_posted_within_last_6_months_view, name='blogs_within_last_6_months'),
    path('within-last-year', views.get_blogs_posted_within_last_year, name='blogs_within_last_year'),
    path('create', views.create_blog_view, name='created_blog'),
    path('<str:blog_id>', views.get_specific_blog_view, name='get_blog'),
    path('user/<str:uid>', views.get_all_user_blogs_view, name='get_all_user_blogs'),
    path('<str:blog_id>/update', views.update_blog_view, name='update_blog'),
    path('<str:blog_id>/delete', views.delete_blog_view, name='delete_blog'),
]