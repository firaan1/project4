# Generated by Django 2.0.3 on 2018-08-30 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0006_delete_colour'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('code', models.CharField(max_length=7)),
            ],
        ),
    ]
