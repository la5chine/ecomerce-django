# Generated by Django 5.0.6 on 2025-01-17 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date_shipped',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shipped',
        ),
    ]
