# Generated by Django 4.0.1 on 2023-05-06 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rahbarlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism_familiya', models.CharField(max_length=255)),
                ('lavozim', models.CharField(max_length=255)),
                ('telefon', models.CharField(max_length=255)),
                ('mail', models.CharField(max_length=255)),
                ('qabul_qilish', models.CharField(max_length=555)),
            ],
        ),
    ]
