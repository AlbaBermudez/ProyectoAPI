# Generated by Django 4.0.3 on 2022-05-18 18:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appAPI', '0004_categoria_articulo_categorias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='categorias',
        ),
        migrations.AddField(
            model_name='articulo',
            name='Created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articulo',
            name='Updated',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='categoria',
        ),
    ]
