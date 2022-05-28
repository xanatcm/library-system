# Generated by Django 3.2 on 2022-05-27 21:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('adress', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('uuid', models.UUIDField(default=uuid.UUID('bb5f6d18-86b6-4d61-a671-21514d037f00'))),
                ('status', models.BooleanField(default=False)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraries.library')),
            ],
        ),
    ]