# Generated by Django 4.1.6 on 2023-02-09 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_rename_strategy_id_trade_strategy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='id',
            field=models.CharField(max_length=4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='trade',
            name='strategy',
            field=models.CharField(max_length=20),
        ),
    ]
