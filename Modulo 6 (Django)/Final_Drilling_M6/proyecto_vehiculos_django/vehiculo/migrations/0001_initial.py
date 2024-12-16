# Generated by Django 5.1.4 on 2024-12-16 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(choices=[('fiat', 'Fiat'), ('chevrolet', 'Chevrolet'), ('ford', 'Ford'), ('toyota', 'Toyota')], default='ford', max_length=20)),
                ('modelo', models.CharField(max_length=100)),
                ('serial_carroceria', models.CharField(max_length=50, unique=True)),
                ('serial_motor', models.CharField(max_length=50, unique=True)),
                ('categoria', models.CharField(choices=[('particular', 'Particular'), ('transporte', 'Transporte'), ('carga', 'Carga')], default='particular', max_length=20)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_de_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_de_modificacion', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
