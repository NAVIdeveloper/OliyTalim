# Generated by Django 4.0.1 on 2023-05-09 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApp', '0004_alter_new_img_2_alter_new_img_3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ariza',
            name='cv',
        ),
        migrations.RemoveField(
            model_name='ishlar',
            name='namuna_cv',
        ),
        migrations.AddField(
            model_name='ishlar',
            name='maosh',
            field=models.CharField(blank=True, max_length=555, null=True),
        ),
        migrations.AddField(
            model_name='new',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
