# Generated by Django 2.0.4 on 2018-04-05 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aggregation', '0004_avitoobject_mindescription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avitoobject',
            name='minDescription',
        ),
        migrations.AddField(
            model_name='mainadobject',
            name='minDescription',
            field=models.CharField(blank=True, max_length=500, verbose_name='Описание'),
        ),
    ]