# Generated by Django 3.0.3 on 2020-02-17 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_auto_20200217_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserId', models.CharField(max_length=30)),
                ('Name', models.CharField(max_length=100)),
                ('Channel_Name', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=100)),
                ('Date', models.CharField(max_length=10)),
                ('Time', models.CharField(max_length=10)),
                ('Image', models.ImageField(default='media/profile.jpeg', upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Videos_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Video_Id', models.CharField(default='', max_length=30)),
                ('Title', models.CharField(max_length=100)),
                ('Channel_Name', models.CharField(max_length=100)),
                ('Category', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=1000)),
                ('Views', models.IntegerField(default=0)),
                ('Likes', models.IntegerField(default=0)),
                ('Comments', models.CharField(max_length=1000)),
                ('Date', models.CharField(max_length=10)),
                ('Time', models.CharField(max_length=10)),
                ('Thumb', models.ImageField(upload_to='media')),
                ('Video', models.FileField(upload_to='media')),
            ],
        ),
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.DeleteModel(
            name='Videos',
        ),
    ]
