# Generated by Django 5.1.3 on 2024-12-03 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputbookmodel',
            name='valoracion',
            field=models.IntegerField(max_length=10000),
        ),
    ]