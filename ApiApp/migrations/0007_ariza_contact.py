# Generated by Django 4.0.1 on 2023-05-09 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApp', '0006_rahbarlar_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='ariza',
            name='contact',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
