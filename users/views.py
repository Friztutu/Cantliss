# settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, reverse
from django.urls import reverse_lazy
from django.contrib import auth, messages

# base views
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView

# base forms
from users.forms import UserRegistrationForm, UserProfileForm, UserLoginForm

# models
from basket.models import Basket
from users.models import CustomUser


class UserRegistrationView(CreateView):
    model = CustomUser
    template_name = 'users/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super(UserRegistrationView, self).get_context_data()
        context['title'] = 'Регистрация'
        return context


class UserProfileView(UpdateView):
    model = CustomUser
    template_name = 'users/profile.html'
    form_class = UserProfileForm

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['title'] = 'Профиль'
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.request.user.id,))


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.request.user.id,))


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('products:index'))
