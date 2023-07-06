# Generated by Django 4.0.1 on 2023-07-06 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApp', '0009_hududlar'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaholashMezon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OTM_nomi', models.CharField(max_length=555)),
                ('biriktirilgan_masul', models.CharField(max_length=555)),
                ('kelganligi', models.IntegerField(default=0)),
                ('tekshirish', models.BooleanField()),
            ],
        ),
    ]
