# Generated by Django 4.2 on 2023-05-02 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_wallet', '0002_stock_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='Preco',
            field=models.FloatField(default=2),
            preserve_default=False,
        ),
    ]
