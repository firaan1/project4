# Generated by Django 2.0.3 on 2018-08-30 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0008_kurtarate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kurtarate',
            name='image',
            field=models.ManyToManyField(related_name='kurta_image', to='shopping.Document'),
        ),
    ]
