# Generated by Django 4.2.6 on 2023-11-01 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servinorte_r', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventarios',
            name='total_inventario',
            field=models.FloatField(help_text='El total del inventario. '),
        ),
    ]
