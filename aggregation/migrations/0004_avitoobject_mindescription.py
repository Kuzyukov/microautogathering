# Generated by Django 2.0.4 on 2018-04-05 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aggregation', '0003_auto_20180404_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='avitoobject',
            name='minDescription',
            field=models.CharField(blank=True, max_length=500, verbose_name='Описание'),
        ),
    ]
