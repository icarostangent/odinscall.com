# Generated by Django 3.2.20 on 2023-08-11 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_emailaddress_verify_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='subscription_id',
        ),
        migrations.AddField(
            model_name='subscription',
            name='client_reference_id',
            field=models.CharField(default='FCU9O0gHeMJJ7d86aUS1nzizMaUO943A', max_length=255),
        ),
        migrations.AlterField(
            model_name='emailaddress',
            name='verify_key',
            field=models.CharField(default='nP97LaG7ryn1aVLgP4i9hUkLjD8Ggp6Z', max_length=255, null=True),
        ),
    ]
