# Generated by Django 4.1.7 on 2023-04-26 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='integrantes',
            name='grupo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='usuarios.proyecto', verbose_name='Grupo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='nombre',
            field=models.CharField(max_length=45, verbose_name='Nombre del Grupo'),
        ),
    ]