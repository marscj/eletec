# Generated by Django 3.0.3 on 2020-03-12 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0009_auto_20200312_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='sorter',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='app',
            unique_together={('sorter', 'tag')},
        ),
    ]
