# Generated by Django 4.0.4 on 2022-10-21 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_delete_precios_delete_trabajos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productofijo',
            name='type',
        ),
        migrations.AddField(
            model_name='productofijo',
            name='cantidades',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
