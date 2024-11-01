# Generated by Django 5.1.1 on 2024-10-29 23:49

import CrudTrabajadores.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_area', models.CharField(max_length=50)),
                ('tipo_area', models.CharField(choices=[('Marketing', 'Marketing'), ('Finanzas', 'Finanzas'), ('Logistica', 'Logística'), ('IT', 'IT'), ('Ventas', 'Ventas'), ('Administrativa', 'Administrativa')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CargaFamiliar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_carga', models.CharField(max_length=50)),
                ('relacion', models.CharField(max_length=50)),
                ('grupo_salud', models.CharField(choices=[('Fonasa', 'Fonasa'), ('Isapre', 'Isapre')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_departamento', models.CharField(max_length=50)),
                ('ubicacion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_ingreso', models.DateField()),
                ('estado_activo', models.BooleanField(default=True, validators=[CrudTrabajadores.models.validate_active_status])),
            ],
        ),
    ]
