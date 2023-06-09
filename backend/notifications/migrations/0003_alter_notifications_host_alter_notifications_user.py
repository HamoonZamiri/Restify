# Generated by Django 4.1.7 on 2023-04-18 00:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notifications', '0002_alter_notifications_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='host',
            field=models.ForeignKey(limit_choices_to={'account_type': 'Host'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='host', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='user',
            field=models.ForeignKey(limit_choices_to={'account_type': 'User'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
