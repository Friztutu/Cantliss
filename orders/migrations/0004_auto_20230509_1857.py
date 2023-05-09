# Generated by Django 3.2.18 on 2023-05-09 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20230509_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_paid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.AddField(
            model_name='order',
            name='basket_history',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Создан'), (1, 'Оплачен'), (2, 'В пути'), (3, 'Доставлен')], default=0),
        ),
    ]