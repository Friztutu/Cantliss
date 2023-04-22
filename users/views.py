from django.shortcuts import render

# Create your views here.

def profile(request):
    context = {
        'title': 'Profile',
    }
    return render(request, 'users/profile.html', context=context)


def register(request):
    context = {
        'title': 'Register',
    }
    return render(request, 'users/register.html', context=context)


def login(request):
    context = {
        'title': 'Login',
    }
    return render(request, 'users/login.html', context=context)
