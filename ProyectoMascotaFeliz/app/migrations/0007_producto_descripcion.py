# Generated by Django 4.0.4 on 2022-07-12 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_cliente_nombrecliente_alter_cliente_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(default='descripcion', max_length=100, verbose_name='Descripcion'),
        ),
    ]
