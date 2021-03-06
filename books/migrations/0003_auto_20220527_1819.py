# Generated by Django 3.2 on 2022-05-27 23:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20220527_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bookitem',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('87a0b0ca-0d87-43f5-a304-28111ce3374a'), editable=False),
        ),
    ]
