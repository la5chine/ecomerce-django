# Generated by Django 5.0.6 on 2025-01-17 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_remove_order_date_shipped_remove_order_shipped'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount_paid',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
