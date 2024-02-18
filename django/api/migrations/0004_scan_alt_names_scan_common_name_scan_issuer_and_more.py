# Generated by Django 4.2.9 on 2024-02-16 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_scan_ip_scan_ip_address_alter_scan_port'),
    ]

    operations = [
        migrations.AddField(
            model_name='scan',
            name='alt_names',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='scan',
            name='common_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='scan',
            name='issuer',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='scan',
            name='not_after',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='scan',
            name='not_before',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='scan',
            name='serial_number',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
