from . import views
from django.urls import path

urlpatterns = [
    path('signup', views.signup, name='sign_up'),
    path('verify-user', views.verify_user, name='verify_user'),
    path('login', views.login, name='login'),
    path('reset-password', views.password_reset, name='password_reset'),
    path('password-reset-confirm', views.password_reset_confirm, name='password_reset_confirm'),
    path('all-users', views.get_all_users, name='get_all_users'),
    path('search', views.search_users, name='search_users')
]