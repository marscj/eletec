# Generated by Django 3.0 on 2020-01-13 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    atomic = False
    
    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(blank=True, default='nhka', max_length=4, null=True),
        ),
        migrations.AlterModelTable(
            name='order',
            table='order',
        ),
    ]
