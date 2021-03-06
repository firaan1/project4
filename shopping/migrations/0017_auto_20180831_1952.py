# Generated by Django 2.0.3 on 2018-08-31 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0016_auto_20180831_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sareerate',
            name='size',
            field=models.ManyToManyField(related_name='saree_size', to='shopping.SareeSize'),
        ),
        migrations.AlterField(
            model_name='toprate',
            name='size',
            field=models.ManyToManyField(related_name='top_size', to='shopping.TopSize'),
        ),
        migrations.AlterField(
            model_name='trouserrate',
            name='size',
            field=models.ManyToManyField(related_name='trouser_size', to='shopping.TrouserSize'),
        ),
    ]
