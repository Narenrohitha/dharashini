# Generated by Django 4.0.3 on 2022-03-06 08:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('des', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 3, 6, 14, 23, 18, 583984))),
            ],
        ),
    ]
