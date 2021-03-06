# Generated by Django 3.2.6 on 2022-05-16 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('xoki', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_de_reporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('tipo_de_reporte', models.IntegerField()),
                ('creado_por_el_habitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xoki.habitante')),
            ],
        ),
    ]
