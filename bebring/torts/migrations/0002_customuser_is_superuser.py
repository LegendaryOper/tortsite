# Generated by Django 4.0.2 on 2022-04-25 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
