# Generated by Django 5.0.7 on 2025-03-07 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='dropoff_location',
            new_name='dropoff_street_address',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='pickup_location',
            new_name='pickup_street_address',
        ),
        migrations.AddField(
            model_name='booking',
            name='dropoff_city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='dropoff_state',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='dropoff_zip_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='pickup_city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='pickup_state',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='pickup_zip_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
