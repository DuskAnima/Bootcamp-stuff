# Generated by Django 5.1.3 on 2024-12-07 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listbook', '0002_alter_inputbookmodel_valoracion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inputbookmodel',
            options={'permissions': (('development', 'Permiso como desarrollador'), ('scrum_master', 'Permiso como Scrum Master'), ('product_owner', 'Permiso como Product Owner'))},
        ),
    ]
