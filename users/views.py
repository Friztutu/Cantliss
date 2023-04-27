from django.shortcuts import render
from users.forms import UserRegistrationForm, UserProfileForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, reverse
from django.contrib import auth
from basket.models import Basket


# Create your views here.

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))

    else:
        form = UserProfileForm(instance=request.user)

    context = {
        'title': 'Profile',
        'form': form,
        'baskets': Basket.objects.filter(user=request.user),
    }
    return render(request, 'users/profile.html', context=context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))

    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Profile',
        'form': form
    }
    return render(request, 'users/register.html', context=context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users:profile'))

    else:
        form = UserLoginForm()

    context = {
        'title': 'Profile',
        'form': form
    }
    return render(request, 'users/login.html', context=context)


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('products:index'))
