# Generated by Django 2.1.7 on 2019-04-06 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='connect',
            name='summary',
            field=models.TextField(default='this is cool'),
        ),
    ]
