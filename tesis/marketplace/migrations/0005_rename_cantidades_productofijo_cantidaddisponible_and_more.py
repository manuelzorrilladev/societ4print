# Generated by Django 4.0.4 on 2022-10-27 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0004_remove_productofijo_type_productofijo_cantidades'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productofijo',
            old_name='cantidades',
            new_name='cantidadDisponible',
        ),
        migrations.AddField(
            model_name='productofijo',
            name='cantidadVendida',
            field=models.PositiveIntegerField(default=0),
        ),
    ]