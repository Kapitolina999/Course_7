# Generated by Django 4.0.1 on 2022-12-26 15:57

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TgUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_chat_id', models.BigIntegerField()),
                ('tg_user_id', models.BigIntegerField(unique=True)),
                ('username', models.CharField(blank=True, max_length=32, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='tg_username')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'TG пользователь',
                'verbose_name_plural': 'TG пользователи',
            },
        ),
    ]