# Generated by Django 5.0.2 on 2024-03-05 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_level', models.CharField(max_length=200)),
                ('service_type', models.CharField(max_length=200)),
                ('currency', models.CharField(max_length=200)),
            ],
        ),
    ]