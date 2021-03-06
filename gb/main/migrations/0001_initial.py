# Generated by Django 3.0.5 on 2020-04-12 11:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('qty', models.IntegerField(default=0)),
                ('status', models.CharField(default='', max_length=15)),
                ('date', models.DateField(default=datetime.date.today)),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
    ]
