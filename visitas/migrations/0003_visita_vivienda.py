# Generated by Django 3.2.6 on 2022-05-16 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xoki', '0002_vivienda_nombre'),
        ('visitas', '0002_auto_20220516_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='visita',
            name='vivienda',
            field=models.ForeignKey(default=str, on_delete=django.db.models.deletion.CASCADE, to='xoki.vivienda'),
            preserve_default=False,
        ),
    ]
