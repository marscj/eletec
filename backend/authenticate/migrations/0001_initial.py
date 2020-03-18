# Generated by Django 3.0.3 on 2020-03-18 06:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneConfirmation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(blank=True, max_length=4, null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'phone_confirmation',
            },
        ),
        migrations.CreateModel(
            name='EmailAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=128, unique=True)),
                ('verified', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='email_address', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'email_address',
            },
        ),
    ]
