# Generated by Django 2.0.3 on 2018-09-02 07:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0034_auto_20180901_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinput',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]