# Generated by Django 4.2.4 on 2023-08-17 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_carritoitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='carritoitem',
            name='precio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]