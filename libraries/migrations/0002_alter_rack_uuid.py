# Generated by Django 3.2 on 2022-05-27 23:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('2c2896d2-3e62-412f-848d-058d3498b066')),
        ),
    ]
