from django.urls import path
from .views import signin, register, edit_profile, account_type
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('signup/', register, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(template_name='mainapp/general_home.html'), name='logout'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('account_type/', account_type, name='account_type')


]