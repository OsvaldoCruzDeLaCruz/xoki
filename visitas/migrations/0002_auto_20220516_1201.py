# Generated by Django 3.2.6 on 2022-05-16 17:01

from django.db import migrations, models
import visitas.models


class Migration(migrations.Migration):

    dependencies = [
        ('visitas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visita',
            old_name='apellido',
            new_name='apellido_del_visitante',
        ),
        migrations.RenameField(
            model_name='visita',
            old_name='correo',
            new_name='correo_del_visitante',
        ),
        migrations.RenameField(
            model_name='visita',
            old_name='nombre',
            new_name='nombre_del_visitante',
        ),
        migrations.RenameField(
            model_name='visita',
            old_name='telefono',
            new_name='telefono_del_visitante',
        ),
        migrations.AddField(
            model_name='visita',
            name='codigo_qr',
            field=models.ImageField(blank=True, null=True, upload_to=visitas.models.qr_directory_path),
        ),
    ]
