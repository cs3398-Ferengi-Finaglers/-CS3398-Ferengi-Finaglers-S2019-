# Generated by Django 2.1.7 on 2019-03-02 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0006_auto_20190301_2000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answers',
            old_name='belongsToWhichQuestion',
            new_name='belongsTo',
        ),
        migrations.AlterField(
            model_name='questions',
            name='answertype',
            field=models.CharField(choices=[('SINGLE', 'Single Answer'), ('MULTIPLE', 'Multiple Answers'), ('SORTABLE', 'Sortable/Rateable Answers')], default='SINGLEANSWER', max_length=64, verbose_name='Answer Type'),
        ),
    ]