# Generated by Django 3.0.3 on 2020-03-09 10:18

import app.user.models
from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200309_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to=app.user.models.file_path_name),
        ),
    ]
