# Generated by Django 3.2.20 on 2023-08-23 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20230820_2256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailaddress',
            name='billing',
        ),
        migrations.AddField(
            model_name='subscription',
            name='cancel_at',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='cancel_at_period_end',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='emailaddress',
            name='reset_key',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='emailaddress',
            name='reset_sent',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emailaddress',
            name='verify_key',
            field=models.CharField(blank=True, default='BRFCysZ8qIUo4pfcq6K7dJmpfCc9C6Wt', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='client_reference_id',
            field=models.CharField(default='CfDkdYGrbQbUm2GO82YAHESEO6vqjGBx', max_length=255),
        ),
    ]
