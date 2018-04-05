# Generated by Django 2.0.4 on 2018-04-04 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aggregation', '0002_auto_20180404_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainadobject',
            name='AMru',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aggregation.AMruObject', verbose_name='АМру'),
        ),
        migrations.AlterField(
            model_name='mainadobject',
            name='Avito',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aggregation.AvitoObject', verbose_name='Авито'),
        ),
        migrations.AlterField(
            model_name='mainadobject',
            name='Drom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aggregation.DromObject', verbose_name='Дром'),
        ),
        migrations.AlterField(
            model_name='mainadobject',
            name='Youla',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aggregation.YoulaObject', verbose_name='Юла'),
        ),
    ]