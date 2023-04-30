# settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, reverse
from django.urls import reverse_lazy
from django.contrib import auth
from django.contrib.messages.views import SuccessMessageMixin
from common.views import TitleMixin
from django.views.generic import TemplateView

# base views
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView

# base forms
from users.forms import UserRegistrationForm, UserProfileForm, UserLoginForm

# models
from basket.models import Basket
from users.models import CustomUser, EmailVerification


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = CustomUser
    template_name = 'users/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    success_message = 'Registration successful'
    title = 'Регистрация'


class UserProfileView(TitleMixin, UpdateView):
    model = CustomUser
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    title = 'Профиль'

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.request.user.id,))


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Авторизация'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.request.user.id,))


class EmailVerificationView(TitleMixin, TemplateView):
    template_name = 'users/email_verification.html'
    title = 'Store - Подтверждение электронной почты'

    def get(self, request, *args, **kwargs):
        code = kwargs.get('code')
        user = CustomUser.objects.get(email=kwargs.get('email'))
        email_verify = EmailVerification.objects.filter(user=user, code=code)
        if email_verify:
            user.is_verified = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('products:index'))


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('products:index'))
