from django.urls import path, include
from users.views import UserProfileView, UserLoginView, UserRegistrationView, logout
from django.contrib.auth.decorators import login_required

app_name = 'users'

urlpatterns = [
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('logout/', logout, name='logout'),
]
