# Generated by Django 3.2.6 on 2022-05-16 16:26

from django.db import migrations, models
import django.db.models.deletion
import xoki.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=100)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('contratado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Condomino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vivienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('condominio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xoki.condomino')),
            ],
        ),
        migrations.CreateModel(
            name='Jefe_Condominio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=100)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('administrador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xoki.administrador')),
            ],
        ),
        migrations.CreateModel(
            name='Habitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=100)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('estatus', models.BooleanField(default=True)),
                ('duenio', models.BooleanField(default=False)),
                ('foto', models.ImageField(blank=True, null=True, upload_to=xoki.models.xoki_directory_path)),
                ('vivienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xoki.vivienda')),
            ],
        ),
        migrations.CreateModel(
            name='Guardia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=100)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('contratado', models.BooleanField(default=True)),
                ('trabajando', models.BooleanField(default=True)),
                ('condiminio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xoki.condomino')),
            ],
        ),
        migrations.AddField(
            model_name='condomino',
            name='jefe_Condominio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xoki.jefe_condominio'),
        ),
    ]
