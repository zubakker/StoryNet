# Generated by Django 3.2.5 on 2021-08-06 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20210806_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='photo',
            field=models.ImageField(blank=True, upload_to='avatars'),
        ),
    ]