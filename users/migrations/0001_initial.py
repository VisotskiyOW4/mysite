# Generated by Django 3.2.2 on 2021-05-11 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_surname', models.CharField(max_length=80, verbose_name='Імя та прізвище')),
                ('login', models.CharField(max_length=50, verbose_name='Логін Користувача')),
                ('password', models.CharField(max_length=50, verbose_name='Пароль користувача')),
                ('passport_id', models.CharField(max_length=6, verbose_name='Дані Паспорта')),
                ('gum_status', models.BooleanField(default=False, verbose_name='У залі')),
                ('discount', models.BooleanField(default=False, verbose_name='Знижка')),
            ],
        ),
    ]