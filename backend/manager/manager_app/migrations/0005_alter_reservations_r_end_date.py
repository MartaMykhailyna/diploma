# Generated by Django 5.0.4 on 2024-06-11 15:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager_app', '0004_alter_reservations_r_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='r_end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 11, 18, 37, 45, 78481, tzinfo=datetime.timezone.utc)),
        ),
    ]
