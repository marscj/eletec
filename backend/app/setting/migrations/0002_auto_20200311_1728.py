# Generated by Django 3.0.3 on 2020-03-11 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
