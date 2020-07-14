from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup_page'),
    path('login/', auth_views.LoginView.as_view(template_name="users/login_page.html"), name='login_page'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout_page.html"), name='logout_page'),
    path('profile/', views.profile, name='profile_page'),
]
