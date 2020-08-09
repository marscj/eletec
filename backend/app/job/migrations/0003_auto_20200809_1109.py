# Generated by Django 3.0.3 on 2020-08-09 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20200730_1215'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0002_auto_20200318_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='jobs', to='order.Order'),
        ),
        migrations.AlterField(
            model_name='job',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='jobs', to=settings.AUTH_USER_MODEL),
        ),
    ]
