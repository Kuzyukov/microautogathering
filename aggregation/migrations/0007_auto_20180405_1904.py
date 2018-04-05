# Generated by Django 2.0.4 on 2018-04-05 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aggregation', '0006_auto_20180405_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='moderation',
        ),
        migrations.AlterField(
            model_name='amruobject',
            name='AdName',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название объявления'),
        ),
        migrations.AlterField(
            model_name='amruobject',
            name='Color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aggregation.ColorOfAuto', verbose_name='Цвет автомобиля'),
        ),
        migrations.AlterField(
            model_name='amruobject',
            name='MarkAuto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aggregation.MarkOfAuto', verbose_name='Марка автомобиля'),
        ),
        migrations.AlterField(
            model_name='amruobject',
            name='Mileage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='amruobject',
            name='ModelAuto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aggregation.ModelOfAuto', verbose_name='Модель автомобиля'),
        ),
        migrations.AlterField(
            model_name='amruobject',
            name='Price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='amruobject',
            name='YearOfIssue',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='amruobject',
            name='linkOnAd',
            field=models.CharField(blank=True, max_length=1500, null=True, verbose_name='Ссылка на объявление'),
        ),
        migrations.AlterField(
            model_name='avitoobject',
            name='AdName',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название объявления'),
        ),
        migrations.AlterField(
            model_name='avitoobject',
            name='BodyType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aggregation.BodyTypeOfAuto', verbose_name='Тип кузова автомобиля'),
        ),
        migrations.AlterField(
            model_name='avitoobject',
            name='Color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aggregation.ColorOfAuto', verbose_name='Цвет автомобиля'),
        ),
        migrations.AlterField(
            model_name='avitoobject',
            name='Description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='avitoobject',
            name='DriveUnit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aggregation.DriveUnitOfAuto', verbose_name='Привод'),
        ),
        migrations.AlterField(
            model_name='avitoobject',
            name='EngineCapacity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='avitoobject',
            name='EnginePower',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='avitoobject',
            name='MarkAuto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aggregation.MarkOfAuto', verbose_name='Марка автомобиля'),
        ),
        migrations.AlterField(
            model_name='avitoobject',
            name='Mileage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='avitoobject',
            name='ModelAuto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aggregation.ModelOfAuto', verbose_name='Модель автомобиля'),
        ),
        migrations.AlterField(
            model_name='avitoobject',
            name='NumberOfOwners',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='avitoobject',
            name='Picture',
            field=models.CharField(blank=True, max_length=1500, null=True, verbose_name='Ссылка на изображение'),
        ),
        migrations.AlterField(
            model_name='avitoobject',
            name='Price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='avitoobject',
            name='TransmissionType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aggregation.TransmissionTypeOfAuto', verbose_name='Тип коробки передач'),
        ),
        migrations.AlterField(
            model_name='avitoobject',
            name='YearOfIssue',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='avitoobject',
            name='linkOnAd',
            field=models.CharField(blank=True, max_length=1500, null=True, verbose_name='Ссылка на объявление'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='ad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aggregation.MainAdObject', verbose_name='Комментируемое Объявление'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Текст комментария'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='dromobject',
            name='AdName',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название объявления'),
        ),
        migrations.AlterField(
            model_name='dromobject',
            name='Color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aggregation.ColorOfAuto', verbose_name='Цвет автомобиля'),
        ),
        migrations.AlterField(
            model_name='dromobject',
            name='MarkAuto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aggregation.MarkOfAuto', verbose_name='Марка автомобиля'),
        ),
        migrations.AlterField(
            model_name='dromobject',
            name='Mileage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dromobject',
            name='ModelAuto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aggregation.ModelOfAuto', verbose_name='Модель автомобиля'),
        ),
        migrations.AlterField(
            model_name='dromobject',
            name='Price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dromobject',
            name='YearOfIssue',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dromobject',
            name='linkOnAd',
            field=models.CharField(blank=True, max_length=1500, null=True, verbose_name='Ссылка на объявление'),
        ),
        migrations.AlterField(
            model_name='mainadobject',
            name='AdName',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название объявления'),
        ),
        migrations.AlterField(
            model_name='mainadobject',
            name='BodyType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aggregation.BodyTypeOfAuto', verbose_name='Тип кузова автомобиля'),
        ),
        migrations.AlterField(
            model_name='mainadobject',
            name='Color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aggregation.ColorOfAuto', verbose_name='Цвет автомобиля'),
        ),
        migrations.AlterField(
            model_name='mainadobject',
            name='Description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mainadobject',
            name='DriveUnit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aggregation.DriveUnitOfAuto', verbose_name='Привод'),
        ),
        migrations.AlterField(
            model_name='mainadobject',
            name='EngineCapacity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mainadobject',
            name='EnginePower',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mainadobject',
            name='MarkAuto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aggregation.MarkOfAuto', verbose_name='Марка автомобиля'),
        ),
        migrations.AlterField(
            model_name='mainadobject',
            name='Mileage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mainadobject',
            name='ModelAuto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aggregation.ModelOfAuto', verbose_name='Модель автомобиля'),
        ),
        migrations.AlterField(
            model_name='mainadobject',
            name='NumberOfOwners',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mainadobject',
            name='Picture',
            field=models.CharField(blank=True, max_length=1500, null=True, verbose_name='Ссылка на изображение'),
        ),
        migrations.AlterField(
            model_name='mainadobject',
            name='Price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mainadobject',
            name='TransmissionType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aggregation.TransmissionTypeOfAuto', verbose_name='Тип коробки передач'),
        ),
        migrations.AlterField(
            model_name='mainadobject',
            name='YearOfIssue',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mainadobject',
            name='minDescription',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='youlaobject',
            name='AdName',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название объявления'),
        ),
        migrations.AlterField(
            model_name='youlaobject',
            name='Color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aggregation.ColorOfAuto', verbose_name='Цвет автомобиля'),
        ),
        migrations.AlterField(
            model_name='youlaobject',
            name='MarkAuto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aggregation.MarkOfAuto', verbose_name='Марка автомобиля'),
        ),
        migrations.AlterField(
            model_name='youlaobject',
            name='Mileage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='youlaobject',
            name='ModelAuto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aggregation.ModelOfAuto', verbose_name='Модель автомобиля'),
        ),
        migrations.AlterField(
            model_name='youlaobject',
            name='Price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='youlaobject',
            name='YearOfIssue',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='youlaobject',
            name='linkOnAd',
            field=models.CharField(blank=True, max_length=1500, null=True, verbose_name='Ссылка на объявление'),
        ),
    ]
