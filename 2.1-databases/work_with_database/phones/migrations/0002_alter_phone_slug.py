# Generated by Django 4.2.5 on 2023-09-28 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(verbose_name='Slug'),
        ),
    ]