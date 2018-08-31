# Generated by Django 2.0.3 on 2018-08-31 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0014_auto_20180831_1227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kurtarate',
            name='color',
        ),
        migrations.RemoveField(
            model_name='sareerate',
            name='color',
        ),
        migrations.RemoveField(
            model_name='toprate',
            name='color',
        ),
        migrations.RemoveField(
            model_name='trouserrate',
            name='color',
        ),
        migrations.AddField(
            model_name='document',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dress_color', to='shopping.Color'),
        ),
    ]