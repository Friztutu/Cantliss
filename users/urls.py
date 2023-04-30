# settings
from django.urls import path
from django.contrib.auth.decorators import login_required

# views
from users.views import UserProfileView, UserLoginView, UserRegistrationView, logout, EmailVerificationView


app_name = 'users'

urlpatterns = [
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('logout/', logout, name='logout'),
    path('verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification'),
]
