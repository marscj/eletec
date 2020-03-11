# Generated by Django 3.0.3 on 2020-03-09 10:16

import app.user.models
from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_comment_create_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(default=1, upload_to=app.user.models.file_path_name),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='image_ppoi',
            field=versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(blank=True, default=5, null=True),
        ),
    ]