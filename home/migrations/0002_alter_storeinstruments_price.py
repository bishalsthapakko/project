# Generated by Django 5.1.5 on 2025-01-26 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeinstruments',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
