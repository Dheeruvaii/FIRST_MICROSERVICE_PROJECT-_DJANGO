# Generated by Django 4.2.4 on 2023-08-10 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=100)),
                ('productDescription', models.TextField(max_length=100)),
                ('productPrice', models.IntegerField()),
                ('productQuantity', models.IntegerField()),
                ('productCategory', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
