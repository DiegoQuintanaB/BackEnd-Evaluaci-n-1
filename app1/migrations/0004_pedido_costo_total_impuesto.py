# Generated by Django 4.2.6 on 2023-10-12 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_pedido_costo_envio_clp'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='costo_total_impuesto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
