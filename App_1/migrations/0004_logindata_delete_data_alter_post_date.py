# Generated by Django 5.0.4 on 2024-04-17 14:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_1', '0003_data_alter_post_date_alter_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='loginData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'loginData',
                'verbose_name_plural': 'loginDatas',
            },
        ),
        migrations.DeleteModel(
            name='Data',
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 4, 17, 20, 15, 48, 815736)),
        ),
    ]
