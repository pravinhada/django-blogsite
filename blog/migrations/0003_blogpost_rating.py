# Generated by Django 3.2.3 on 2021-06-02 01:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210601_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='rating',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
