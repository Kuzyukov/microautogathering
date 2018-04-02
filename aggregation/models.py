from django.db import models
from django.contrib.auth import get_user_model

"""
class AvitoObject(models.Model):
    AdName = models.CharField("Ссылка на объявление", max_lenght=100)
    linkOnAd = models.CharField("Ссылка на объявление", max_lenght=1500)
    ModelAuto = models.ForeignKey(ModelOfAuto, verbose_name="Модель автомобиля")
    MarkAuto = models.ForeignKey(MarkOfAuto, verbose_name="Марка автомобиля")
    Price = models.IntegerField()
    YearOfIssue  = models.IntegerField()
    Mileage  = models.IntegerField()
    BodyType = models.ForeignKey(BodyTypeOfAuto, verbose_name="Тип кухова автомобиля")
    Color = models.ForeignKey(ColorOfAuto, verbose_name="Цвет автомобиля")
    EngineCapacity = models.IntegerField()
    kolvoDverey = models.IntegerField()
    TransmissionType = models.ForeignKey(TransmissionTypeOfAuto, verbose_name="Тип коробки передач")
    DriveUnit = models.ForeignKey(DriveUnitOfAuto, verbose_name="Привод")
    NumberOfOwners = models.IntegerField()
    EnginePower = models.IntegerField()
    Description = models.TextField()
    Picture = models.CharField("Ссылка на объявление", max_lenght=1500)

class DromObject(models.Model):
    AdName = models.CharField("Ссылка на объявление", max_lenght=100)
    linkOnAd = models.CharField("Ссылка на объявление", max_lenght=1500)
    ModelAuto = models.ForeignKey(ModelOfAuto, verbose_name="Модель автомобиля")
    MarkAuto = models.ForeignKey(MarkOfAuto, verbose_name="Марка автомобиля")
    YearOfIssue  = models.IntegerField()
    Color = models.ForeignKey(ColorOfAuto, verbose_name="Цвет автомобиля")
    Mileage  = models.IntegerField()
    Price = models.IntegerField()


class AMruObject(models.Model):
    AdName = models.CharField("Ссылка на объявление", max_lenght=100)
    linkOnAd = models.CharField("Ссылка на объявление", max_lenght=1500)
    ModelAuto = models.ForeignKey(ModelOfAuto, verbose_name="Модель автомобиля")
    MarkAuto = models.ForeignKey(MarkOfAuto, verbose_name="Марка автомобиля")
    YearOfIssue  = models.IntegerField()
    Color = models.ForeignKey(ColorOfAuto, verbose_name="Цвет автомобиля")
    Mileage  = models.IntegerField()
    Price = models.IntegerField()

class YoulaObject(models.Model):
    AdName = models.CharField("Ссылка на объявление", max_lenght=100)
    linkOnAd = models.CharField("Ссылка на объявление", max_lenght=1500)
    ModelAuto = models.ForeignKey(ModelOfAuto, verbose_name="Модель автомобиля")
    MarkAuto = models.ForeignKey(MarkOfAuto, verbose_name="Марка автомобиля")
    YearOfIssue  = models.IntegerField()
    Color = models.ForeignKey(ColorOfAuto, verbose_name="Цвет автомобиля")
    Mileage  = models.IntegerField()
    Price = models.IntegerField()



class MainAdObject(models.Model):
    user = models.ForeignKey(User, verbose_name="Автор комментария")
    Avito = models.ForeignKey(AvitoObject, verbose_name="Авито")
    Drom = models.ForeignKey(DromObject, verbose_name="Дром")
    AMru = models.ForeignKey(AMruObject, verbose_name="Дром")
    Youla = models.ForeignKey(YoulaObject, verbose_name="Дром")





class Comments(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=model.CASCADE)
    new = models.ForeignKey(
        MainAdObject,
        verbose_name="Комментируемое Объявление",
        on_delete=model.CASCADE)
"""
