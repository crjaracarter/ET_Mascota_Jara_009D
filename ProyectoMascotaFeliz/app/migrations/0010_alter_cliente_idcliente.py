# Generated by Django 4.0.4 on 2022-07-14 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_cliente_correo_cliente_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='idCliente',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='idCliente'),
        ),
    ]
