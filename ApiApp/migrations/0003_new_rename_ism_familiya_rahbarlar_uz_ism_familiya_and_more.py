# Generated by Django 4.0.1 on 2023-05-09 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApp', '0002_ishlar_ariza'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uz_title', models.CharField(max_length=999)),
                ('uz_text', models.TextField()),
                ('img', models.ImageField(upload_to='news/')),
                ('img_2', models.ImageField(upload_to='news/')),
                ('img_3', models.ImageField(upload_to='news/')),
                ('uz_text_2', models.TextField(blank=True, null=True)),
                ('uz_text_3', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='rahbarlar',
            old_name='ism_familiya',
            new_name='uz_ism_familiya',
        ),
        migrations.RenameField(
            model_name='rahbarlar',
            old_name='lavozim',
            new_name='uz_lavozim',
        ),
        migrations.RenameField(
            model_name='rahbarlar',
            old_name='qabul_qilish',
            new_name='uz_qabul_qilish',
        ),
        migrations.AddField(
            model_name='rahbarlar',
            name='en_lavozim',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rahbarlar',
            name='en_qabul_qilish',
            field=models.CharField(blank=True, max_length=555, null=True),
        ),
        migrations.AddField(
            model_name='rahbarlar',
            name='ru_ism_familiya',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rahbarlar',
            name='ru_lavozim',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rahbarlar',
            name='ru_qabul_qilish',
            field=models.CharField(blank=True, max_length=555, null=True),
        ),
    ]