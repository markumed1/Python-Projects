# Generated by Django 4.0.3 on 2022-03-27 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('treats', 'treats'), ('entrees', 'entrees'), ('drinks', 'drinks'), ('appetizers', 'appetizers')], max_length=60),
        ),
    ]
