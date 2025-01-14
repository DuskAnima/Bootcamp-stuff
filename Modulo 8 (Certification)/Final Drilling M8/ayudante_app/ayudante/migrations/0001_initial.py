# Generated by Django 5.1.4 on 2025-01-11 00:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'ayudante_servicio',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('horarios', models.CharField(max_length=256)),
                ('telefono', models.CharField(max_length=256)),
                ('descripcion', models.CharField(max_length=555)),
                ('foto', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ayudante_proveedor',
            },
        ),
        migrations.CreateModel(
            name='ProveedorMensaje',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('mensaje', models.CharField(max_length=512)),
                ('fecha_registro', models.DateField()),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ayudante.proveedor')),
            ],
            options={
                'db_table': 'ayudante_proveedormensaje',
            },
        ),
        migrations.CreateModel(
            name='ProveedorServicio',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ayudante.proveedor')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ayudante.servicio')),
            ],
            options={
                'db_table': 'ayudante_proveedorservicio',
            },
        ),
    ]
