# Generated by Django 5.1.3 on 2024-12-07 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listbook', '0003_alter_inputbookmodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputbookmodel',
            name='valoracion',
            field=models.IntegerField(),
        ),
    ]
