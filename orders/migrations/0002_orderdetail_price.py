# Generated by Django 3.1.6 on 2021-02-08 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='price',
            field=models.DecimalField(decimal_places=2, default=20, max_digits=15),
            preserve_default=False,
        ),
    ]
