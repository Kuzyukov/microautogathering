from django.db import models
from django.contrib.auth import get_user_model








class AutoRuImages(models.Model):
    AutoRuId = models.ForeignKey(AutoRuObject, verbose_name="АвтоРуКартинка")
    ImageLink = models.CharField("Ссылка на объявление", max_lenght=500)

class AutoRuObject(models.Model):
    """
    Название объявления
    Ссылка на объявление
    Картинки
    Модель
    Марка
    Тип кузова
    Цвет
    Пробег
    Год выпуска
    Тип двигателя (бензин\дизель)
    Тип коробки передач
    Привод
    Объём двигателя
    Мощьность двигателя
    Дата загрузки объявления на сайт
    Количество владельцев
    Описание
    Наличие документов (да/нет)
    На ходу (да/нет)
    Обмен (да/нет)
    Дата, когда объявление было загружено в базу
    """
    AdName = models.CharField("Ссылка на объявление", max_lenght=500)
    linkOnAd = models.CharField("Ссылка на объявление", max_lenght=500)
    ModelAuto = models.ForeignKey(ModelOfAuto, verbose_name="Модель автомобиля")
    MarkAuto = models.ForeignKey(MarkOfAuto, verbose_name="Марка автомобиля")
    BodyType = models.ForeignKey(BodyTypeOfAuto, verbose_name="Тип кухова автомобиля")
    Color = models.ForeignKey(ColorOfAuto, verbose_name="Цвет автомобиля")
    Mileage  = models.IntegerField()
    YearOfIssue  = models.IntegerField()
    EngineType = models.BooleanField()
    TransmissionType = models.ForeignKey(TransmissionTypeOfAuto, verbose_name="Тип коробки передач")
    DriveUnit = models.ForeignKey(DriveUnitOfAuto, verbose_name="Привод")
    EngineCapacity = models.IntegerField()
    EnginePower = models.IntegerField()
    DateOfPublic = models.DateTimeField()
    NumberOfOwners = models.IntegerField()
    Description = models.TextField()
    AvailabilityOfDocuments = models.DateTimeField()
    Condition = models.BooleanField()
    Swap = models.BooleanField()
    DateParcing = models.DateTimeField("Дата, когда объявление было загружено(парсером) в базу", auto_now_add=True)

class AvitoImages(models.Model):
    AutoRuId = models.ForeignKey(AutoRuObject, verbose_name="АвтоРуКартинка")
    ImageLink = models.CharField("Ссылка на объявление", max_lenght=500)

class AvitoObject(models.Model):
    AdName = models.CharField("Ссылка на объявление", max_lenght=500)
    linkOnAd = models.CharField("Ссылка на объявление", max_lenght=500)
    ModelAuto = models.ForeignKey(ModelOfAuto, verbose_name="Модель автомобиля")
    MarkAuto = models.ForeignKey(MarkOfAuto, verbose_name="Марка автомобиля")
    BodyType = models.ForeignKey(BodyTypeOfAuto, verbose_name="Тип кухова автомобиля")
    Color = models.ForeignKey(ColorOfAuto, verbose_name="Цвет автомобиля")
    Mileage  = models.IntegerField()
    YearOfIssue  = models.IntegerField()
    EngineType = models.BooleanField()
    TransmissionType = models.ForeignKey(TransmissionTypeOfAuto, verbose_name="Тип коробки передач")
    DriveUnit = models.ForeignKey(DriveUnitOfAuto, verbose_name="Привод")
    EngineCapacity = models.IntegerField()
    EnginePower = models.IntegerField()
    DateOfPublic = models.DateTimeField()
    NumberOfOwners = models.IntegerField()
    Description = models.TextField()
    AvailabilityOfDocuments = models.DateTimeField()
    Condition = models.BooleanField()
    Swap = models.BooleanField()
    DateParcing = models.DateTimeField("Дата, когда объявление было загружено(парсером) в базу", auto_now_add=True)

class DromImages(models.Model):
    AutoRuId = models.ForeignKey(AutoRuObject, verbose_name="АвтоРуКартинка")
    ImageLink = models.CharField("Ссылка на объявление", max_lenght=500)

class DromObject(models.Model):
    AdName = models.CharField("Ссылка на объявление", max_lenght=500)
    linkOnAd = models.CharField("Ссылка на объявление", max_lenght=500)
    ModelAuto = models.ForeignKey(ModelOfAuto, verbose_name="Модель автомобиля")
    MarkAuto = models.ForeignKey(MarkOfAuto, verbose_name="Марка автомобиля")
    BodyType = models.ForeignKey(BodyTypeOfAuto, verbose_name="Тип кухова автомобиля")
    Color = models.ForeignKey(ColorOfAuto, verbose_name="Цвет автомобиля")
    Mileage  = models.IntegerField()
    YearOfIssue  = models.IntegerField()
    EngineType = models.BooleanField()
    TransmissionType = models.ForeignKey(TransmissionTypeOfAuto, verbose_name="Тип коробки передач")
    DriveUnit = models.ForeignKey(DriveUnitOfAuto, verbose_name="Привод")
    EngineCapacity = models.IntegerField()
    EnginePower = models.IntegerField()
    DateOfPublic = models.DateTimeField()
    NumberOfOwners = models.IntegerField()
    Description = models.TextField()
    AvailabilityOfDocuments = models.DateTimeField()
    Condition = models.BooleanField()
    Swap = models.BooleanField()
    DateParcing = models.DateTimeField("Дата, когда объявление было загружено(парсером) в базу", auto_now_add=True)


class MainAdObject(models.Model):
    user = models.ForeignKey(User, verbose_name="Автор комментария")
    AutoRu = models.ForeignKey(AutoRuObject, verbose_name="АвтоРУ")
    Avito = models.ForeignKey(AvitoObject, verbose_name="Авито")
    Drom = models.ForeignKey(DromObject, verbose_name="Дром")
class Comments(models.Model)
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=model.CASCADE)
    new = models.ForeignKey(
        MainAdObject,
        verbose_name="Комментируемое Объявление",
        on_delete=model.CASCADE)
