# Generated by Django 5.1.4 on 2024-12-27 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos_del_proyecto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(default=0),
        ),
    ]
