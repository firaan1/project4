# Generated by Django 2.0.3 on 2018-08-31 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0013_auto_20180830_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kurtarate',
            name='size',
        ),
        migrations.AddField(
            model_name='kurtarate',
            name='size',
            field=models.ManyToManyField(related_name='kurta_size', to='shopping.KurtaSize'),
        ),
    ]
