# Generated by Django 4.0.3 on 2022-05-18 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appAPI', '0005_remove_articulo_categorias_articulo_created_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articulo',
            options={'verbose_name': 'articulo', 'verbose_name_plural': 'articulos'},
        ),
    ]