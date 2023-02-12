# Generated by Django 4.1.6 on 2023-02-09 15:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0004_trade_price_trade_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='pnldata',
            name='capture_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='pnldata',
            name='value',
            field=models.FloatField(default=0),
        ),
    ]
