# Generated by Django 3.2.2 on 2021-05-12 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_prod', models.CharField(max_length=20, verbose_name='Назва товару')),
                ('text_prod', models.TextField(verbose_name='Опис Товару')),
                ('date', models.DateField(verbose_name='Дата публікації')),
                ('prod_img', models.FileField(upload_to='', verbose_name='Фото продукта')),
                ('county', models.CharField(max_length=20, verbose_name='Країна виробник')),
                ('brand', models.CharField(max_length=20, verbose_name='Бренд')),
                ('price_prod', models.FloatField(verbose_name='Ціна товару')),
            ],
        ),
    ]
