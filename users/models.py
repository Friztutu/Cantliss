# base models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail


# Create your models here.

class CustomUser(AbstractUser):
    img = models.ImageField(upload_to=r'user_img', default=r'user_img/default.jpg')
    is_verified_email = models.BooleanField(default=False)

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
        send_mail(
            "Subject here",
            "Here is the message.",
            "from@example.com",
            [self.user.email],
            fail_silently=False,
        )
