from django.urls import path, include
from users.views import ProfileView, login, RegistrationView, logout
from django.contrib.auth.decorators import login_required

app_name = 'users'

urlpatterns = [
    path('profile/<int:pk>/', login_required(ProfileView.as_view()), name='profile'),
    path('login/', login, name='login'),
    path('register', RegistrationView.as_view(), name='register'),
    path('logout', logout, name='logout'),
]

