# Generated by Django 4.1 on 2022-08-28 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ustink', '0002_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user',
            new_name='customer',
        ),
    ]
