# Generated by Django 3.0.3 on 2020-03-14 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('card', models.CharField(blank=True, max_length=16, null=True)),
                ('unit', models.IntegerField(blank=True, null=True)),
                ('remark', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'job',
            },
        ),
    ]
