# Generated by Django 5.1.4 on 2024-12-25 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='autor',
            new_name='author',
        ),
    ]
