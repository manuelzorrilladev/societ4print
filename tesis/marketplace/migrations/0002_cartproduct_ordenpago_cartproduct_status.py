# Generated by Django 4.0.4 on 2022-09-18 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartproduct',
            name='ordenPago',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cartproduct',
            name='status',
            field=models.CharField(default='En proceso', max_length=20),
        ),
    ]