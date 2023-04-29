from django.shortcuts import render
from users.forms import UserRegistrationForm, UserProfileForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, reverse
from django.urls import reverse_lazy
from django.contrib import auth, messages
from basket.models import Basket
from django.views.generic.edit import CreateView, UpdateView
from users.models import CustomUser


# Create your views here.


class RegistrationView(CreateView):
    model = CustomUser
    template_name = 'users/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:profile')

    def get_context_data(self, **kwargs):
        context = super(RegistrationView, self).get_context_data()
        context['title'] = 'Регистрация'
        return context


class ProfileView(UpdateView):
    model = CustomUser
    template_name = 'users/profile.html'
    form_class = UserProfileForm

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data()
        context['title'] = 'Профиль'
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.request.user.id, ))


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users:profile', args=(request.user.id, )))

    else:
        form = UserLoginForm()

    context = {
        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context=context)


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('products:index'))
