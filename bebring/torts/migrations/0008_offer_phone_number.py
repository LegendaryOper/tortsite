# Generated by Django 4.0.2 on 2022-04-12 09:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torts', '0007_tort_main_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='phone_number',
            field=models.CharField(max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]