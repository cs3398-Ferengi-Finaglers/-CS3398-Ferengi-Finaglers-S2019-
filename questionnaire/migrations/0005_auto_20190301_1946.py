# Generated by Django 2.1.7 on 2019-03-02 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0004_auto_20190301_1917'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name_plural': ('Categories',)},
        ),
        migrations.RemoveField(
            model_name='answers',
            name='belongsToWhichQuestion',
        ),
        migrations.AlterField(
            model_name='answers',
            name='KNNvalue',
            field=models.FloatField(verbose_name='What is the KNN value of this answer?'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='category',
            field=models.CharField(default=1, max_length=250, unique=True, verbose_name='Category'),
            preserve_default=False,
        ),
    ]
