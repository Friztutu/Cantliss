from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from users.models import CustomUser, EmailVerification

# Create your tests here.

class UserRegistrationViewTestCase(TestCase):

    def setUp(self):
        self.path = reverse('users:register')
        self.data = {
            'first_name': 'Alex', 'last_name': 'Erofeev',
            'email': 'alexerofeev@gmail.com', 'username': 'fr1zmate',
            'password1': '65toteda', 'password2': '65toteda'
        }

    def test_view(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Регистрация')
        self.assertTemplateUsed('users/register.html')

    def test_post_request_success(self):
        response = self.client.post(path=self.path, data=self.data)
        user = CustomUser.objects.filter(username=self.data['username'])
        email_verify = EmailVerification.objects.filter(user__username=self.data['username'])

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertTrue(user.exists())
        self.assertRedirects(response=response, expected_url=reverse('users:login'))
        self.assertTrue(email_verify.exists())

    def test_post_request_failure(self):
        CustomUser.objects.create(
            username=self.data['username'],
            email=self.data['email'],
        )
        self.data['password1'] = '1234'
        self.data['password2'] = '1234'
        response = self.client.post(path=self.path, data=self.data)

        self.assertContains(response=response, text='Пользователь с таким именем уже существует.')
        self.assertContains(response=response, text='User с таким Email уже существует.')
        self.assertContains(
            response=response,
            text='Введённый пароль слишком короткий. Он должен содержать как минимум 8 символов.'
        )
        self.assertContains(
            response=response,
            text='Введённый пароль состоит только из цифр.'
        )

        # NOT SAME PASSWWORD1 AND PASSWWORD2
        self.data['password1'] = '65toteda'
        self.data['password2'] = '65toteda1'

        response = self.client.post(path=self.path, data=self.data)

        self.assertContains(response=response, text='Введенные пароли не совпадают.')


class UserLoginViewTestCase(TestCase):
    fixtures = ('users.json', )

    def setUp(self) -> None:
        self.path = reverse('users:login')
        self.data = {
            'username': 'sanylz234',
            'password': '1234'
        }

    def test_view(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Авторизация')
        self.assertTemplateUsed('users/login.html')

    def test_post_request_success(self):
        response = self.client.post(path=self.path, data=self.data)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response=response, expected_url=reverse('users:profile', args=(1, )))

    def test_post_request_failure(self):
        self.data['password'] = '12345'
        response = self.client.post(path=self.path, data=self.data)

        self.assertContains(
            response=response,
            text='Пожалуйста, введите правильные имя пользователя и пароль. '
                 'Оба поля могут быть чувствительны к регистру.'
        )


class UserProfileViewTestCase(TestCase):
    fixtures = ('users.json', )

    def setUp(self):
        self.path = reverse('users:profile', args=(1, ))

    def test_view_none_auth(self):
        response = self.client.get(path=self.path)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login') + '?next=/profile/1/')

    def test_view_auth(self):
        login_path = reverse('users:login')
        data = {
            'username': 'sanylz234',
            'password': '1234'
        }
        response_login = self.client.post(login_path, data=data)

        self.assertEqual(response_login.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response=response_login, expected_url=reverse('users:profile', args=(1,)))

        response = self.client.get(path=self.path)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['title'], 'Профиль')
        self.assertTemplateUsed(response, 'users/profile.html')
        self.assertContains(response, text='sanylz234')
        self.assertContains(response, text='Александр')
        self.assertContains(response, text='Erofeev')
        self.assertContains(response, text='alexerof9@gmail.com')
