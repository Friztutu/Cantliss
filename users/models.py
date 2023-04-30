# base models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings


# Create your models here.

class CustomUser(AbstractUser):
    img = models.ImageField(upload_to=r'user_img', default=r'user_img/default.jpg')
    is_verified_email = models.BooleanField(default=False)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f'Code for {self.user}'

    def send_verification_email(self):
        link = reverse('users:email_verification', kwargs={'email': self.user.email, 'code': self.code})
        verify_link = settings.DOMAIN_NAME + link
        send_mail(
            subject="Потверждение электронной почты",
            message=f"{self.user.first_name}, перейдите по ссылке для потверждения электронной почты\n {verify_link}",
            from_email="from@example.com",
            recipient_list=[self.user.email],
            fail_silently=False,
        )
