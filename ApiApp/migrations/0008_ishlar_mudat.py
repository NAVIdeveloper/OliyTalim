# Generated by Django 4.0.1 on 2023-05-11 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApp', '0007_ariza_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='ishlar',
            name='mudat',
            field=models.DateField(auto_now=True),
        ),
    ]
