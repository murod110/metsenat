# Generated by Django 5.0.6 on 2024-05-15 11:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='std_type',
            new_name='type',
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='dt',
            field=models.DateField(default=datetime.datetime(2024, 5, 15, 16, 16, 22, 905284)),
        ),
        migrations.AlterField(
            model_name='student',
            name='dt',
            field=models.DateField(default=datetime.datetime(2024, 5, 15, 16, 16, 22, 905284)),
        ),
    ]
