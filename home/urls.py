from django.urls import path
from home.views import (
    HomeView,
    ProfileView,
    SignUpView,
    CustomLoginView,
    CustomLogoutView, 
    ChangePasswordView
    )

app_name = 'home'

urlpatterns = [
    path('', HomeView, name='home'),
    path('profile/', ProfileView, name='profile'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', SignUpView, name='signup'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('change-password/', ChangePasswordView, name='change_password'),
]