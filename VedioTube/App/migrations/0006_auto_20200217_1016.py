# Generated by Django 3.0.3 on 2020-02-17 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_auto_20200217_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='video_name',
            field=models.FileField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='videos',
            name='video_thumb',
            field=models.ImageField(default='media/profile.jpeg', upload_to='media'),
        ),
    ]
