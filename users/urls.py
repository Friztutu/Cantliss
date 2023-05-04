# settings
from django.contrib.auth.decorators import login_required
from django.urls import path

# views
from users.views import (EmailVerificationView, UserLoginView, UserProfileView,
                         UserRegistrationView, logout)

app_name = 'users'

urlpatterns = [
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('logout/', logout, name='logout'),
    path('verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification'),
]
