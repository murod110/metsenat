# Generated by Django 5.0.6 on 2024-05-20 08:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_contract_amount_student_contract_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='dt',
            field=models.DateField(default=datetime.datetime(2024, 5, 20, 13, 18, 44, 570281)),
        ),
        migrations.AlterField(
            model_name='student',
            name='dt',
            field=models.DateField(default=datetime.datetime(2024, 5, 20, 13, 18, 44, 571872)),
        ),
    ]
