# Generated by Django 5.1.5 on 2025-01-27 10:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_storeinstruments_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='product',
            new_name='instrument',
        ),
        migrations.AddField(
            model_name='cart',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
