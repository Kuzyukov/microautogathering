# Generated by Django 2.0.3 on 2018-04-03 00:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AMruObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkOnAd', models.CharField(max_length=1500, verbose_name='Ссылка на объявление')),
                ('AdName', models.CharField(max_length=100, verbose_name='Название объявления')),
                ('YearOfIssue', models.IntegerField()),
                ('Mileage', models.IntegerField()),
                ('Price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'АМру',
                'verbose_name_plural': 'АМру',
            },
        ),
        migrations.CreateModel(
            name='AvitoObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkOnAd', models.CharField(max_length=1500, verbose_name='Ссылка на объявление')),
                ('AdName', models.CharField(max_length=100, verbose_name='Название объявления')),
                ('Price', models.IntegerField()),
                ('YearOfIssue', models.IntegerField()),
                ('Mileage', models.IntegerField()),
                ('EngineCapacity', models.IntegerField()),
                ('NumberOfOwners', models.IntegerField()),
                ('EnginePower', models.IntegerField()),
                ('Description', models.TextField()),
                ('Picture', models.CharField(max_length=1500, verbose_name='Ссылка на изображение')),
            ],
            options={
                'verbose_name': 'Авито',
                'verbose_name_plural': 'Авито',
            },
        ),
        migrations.CreateModel(
            name='BodyTypeOfAuto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Кузов автомобиля')),
            ],
            options={
                'verbose_name': 'Кузов автомобиля',
                'verbose_name_plural': 'Кузов автомобиля',
            },
        ),
        migrations.CreateModel(
            name='ColorOfAuto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Цвет автомобиля')),
            ],
            options={
                'verbose_name': 'Цвет автомобиля',
                'verbose_name_plural': 'Цвет автомобиля',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата добавления комментария')),
                ('moderation', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='DriveUnitOfAuto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Привод автомобиля')),
            ],
            options={
                'verbose_name': 'Привод автомобиля',
                'verbose_name_plural': 'Привод автомобиля',
            },
        ),
        migrations.CreateModel(
            name='DromObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkOnAd', models.CharField(max_length=1500, verbose_name='Ссылка на объявление')),
                ('AdName', models.CharField(max_length=100, verbose_name='Название объявления')),
                ('YearOfIssue', models.IntegerField()),
                ('Mileage', models.IntegerField()),
                ('Price', models.IntegerField()),
                ('Color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregation.ColorOfAuto', verbose_name='Цвет автомобиля')),
            ],
            options={
                'verbose_name': 'Дром',
                'verbose_name_plural': 'Дром',
            },
        ),
        migrations.CreateModel(
            name='MainAdObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AdName', models.CharField(max_length=100, verbose_name='Название объявления')),
                ('Price', models.IntegerField()),
                ('YearOfIssue', models.IntegerField()),
                ('Mileage', models.IntegerField()),
                ('EngineCapacity', models.IntegerField()),
                ('NumberOfOwners', models.IntegerField()),
                ('EnginePower', models.IntegerField()),
                ('Description', models.TextField()),
                ('Picture', models.CharField(max_length=1500, verbose_name='Ссылка на изображение')),
                ('AMru', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregation.AMruObject', verbose_name='Дром')),
                ('Avito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregation.AvitoObject', verbose_name='Авито')),
                ('BodyType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregation.BodyTypeOfAuto', verbose_name='Тип кузова автомобиля')),
                ('Color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregation.ColorOfAuto', verbose_name='Цвет автомобиля')),
                ('DriveUnit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregation.DriveUnitOfAuto', verbose_name='Привод')),
                ('Drom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregation.DromObject', verbose_name='Дром')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
        migrations.CreateModel(
            name='MarkOfAuto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Марка автомобиля')),
            ],
            options={
                'verbose_name': 'Марка автомобиля',
                'verbose_name_plural': 'Марка автомобиля',
            },
        ),
        migrations.CreateModel(
            name='ModelOfAuto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Модель автомобиля')),
            ],
            options={
                'verbose_name': 'Модель автомобиля',
                'verbose_name_plural': 'Модель автомобиля',
            },
        ),
        migrations.CreateModel(
            name='TransmissionTypeOfAuto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Тип коробки передач автомобиля')),
            ],
            options={
                'verbose_name': 'Тип коробки передач автомобиля',
                'verbose_name_plural': 'Тип коробки передач автомобиля',
            },
        ),
        migrations.CreateModel(
            name='YoulaObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkOnAd', models.CharField(max_length=1500, verbose_name='Ссылка на объявление')),
                ('AdName', models.CharField(max_length=100, verbose_name='Название объявления')),
                ('YearOfIssue', models.IntegerField()),
                ('Mileage', models.IntegerField()),
                ('Price', models.IntegerField()),
                ('Color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregation.ColorOfAuto', verbose_name='Цвет автомобиля')),
                ('MarkAuto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregation.MarkOfAuto', verbose_name='Марка автомобиля')),
                ('ModelAuto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregation.ModelOfAuto', verbose_name='Модель автомобиля')),
            ],
            options={
                'verbose_name': 'Юла',
                'verbose_name_plural': 'Юла',
            },
        ),
        migrations.AddField(
            model_name='mainadobject',
            name='MarkAuto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregation.MarkOfAuto', verbose_name='Марка автомобиля'),
        ),
        migrations.AddField(
            model_name='mainadobject',
            name='ModelAuto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregation.ModelOfAuto', verbose_name='Модель автомобиля'),
        ),
        migrations.AddField(
            model_name='mainadobject',
            name='TransmissionType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregation.TransmissionTypeOfAuto', verbose_name='Тип коробки передач'),
        ),
        migrations.AddField(
            model_name='mainadobject',
            name='Youla',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregation.YoulaObject', verbose_name='Дром'),
        ),
        migrations.AddField(
            model_name='dromobject',
            name='MarkAuto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregation.MarkOfAuto', verbose_name='Марка автомобиля'),
        ),
        migrations.AddField(
            model_name='dromobject',
            name='ModelAuto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregation.ModelOfAuto', verbose_name='Модель автомобиля'),
        ),
        migrations.AddField(
            model_name='comments',
            name='ad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregation.MainAdObject', verbose_name='Комментируемое Объявление'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='avitoobject',
            name='BodyType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregation.BodyTypeOfAuto', verbose_name='Тип кузова автомобиля'),
        ),
        migrations.AddField(
            model_name='avitoobject',
            name='Color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregation.ColorOfAuto', verbose_name='Цвет автомобиля'),
        ),
        migrations.AddField(
            model_name='avitoobject',
            name='DriveUnit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregation.DriveUnitOfAuto', verbose_name='Привод'),
        ),
        migrations.AddField(
            model_name='avitoobject',
            name='MarkAuto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregation.MarkOfAuto', verbose_name='Марка автомобиля'),
        ),
        migrations.AddField(
            model_name='avitoobject',
            name='ModelAuto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregation.ModelOfAuto', verbose_name='Модель автомобиля'),
        ),
        migrations.AddField(
            model_name='avitoobject',
            name='TransmissionType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregation.TransmissionTypeOfAuto', verbose_name='Тип коробки передач'),
        ),
        migrations.AddField(
            model_name='amruobject',
            name='Color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregation.ColorOfAuto', verbose_name='Цвет автомобиля'),
        ),
        migrations.AddField(
            model_name='amruobject',
            name='MarkAuto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregation.MarkOfAuto', verbose_name='Марка автомобиля'),
        ),
        migrations.AddField(
            model_name='amruobject',
            name='ModelAuto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregation.ModelOfAuto', verbose_name='Модель автомобиля'),
        ),
    ]