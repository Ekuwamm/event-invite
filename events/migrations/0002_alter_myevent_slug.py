# Generated by Django 5.1.3 on 2025-01-04 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myevent',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
