from django.urls import path, include
from users.views import profile, login, register, logout

app_name = 'users'

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('login/', login, name='login'),
    path('register', register, name='register'),
    path('logout', logout, name='logout'),
]

