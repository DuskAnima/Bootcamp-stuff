# Generated by Django 5.1.3 on 2024-12-09 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardsmodel',
            name='valor',
            field=models.FloatField(default=0),
        ),
    ]
