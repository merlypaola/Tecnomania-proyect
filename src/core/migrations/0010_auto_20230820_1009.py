# Generated by Django 3.0.7 on 2023-08-20 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_tarjetacredito_usuario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pago',
        ),
        migrations.AlterField(
            model_name='cuentausuario',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='registrousuario',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tarjetacredito',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
