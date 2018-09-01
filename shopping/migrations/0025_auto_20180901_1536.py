# Generated by Django 2.0.3 on 2018-09-01 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0024_placedorder_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placedorder',
            name='status',
            field=models.IntegerField(choices=[('new', 'new'), ('in_progress', 'in_progress'), ('delivered', 'delivered')], default='new'),
        ),
    ]
