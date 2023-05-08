from celery import shared_task
from users.models import CustomUser, EmailVerification
import uuid
from django.utils.timezone import now
from datetime import timedelta


@shared_task
def send_email_verification(user_id):
    user = CustomUser.objects.get(id=user_id)
    expiration = now() + timedelta(hours=48)
    record = EmailVerification.objects.create(code=uuid.uuid4(), expiration=expiration, user=user)
    record.send_verification_email()
