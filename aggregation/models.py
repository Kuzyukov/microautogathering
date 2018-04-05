from django.db import models
from django.contrib.auth import get_user_model
#pip install django-allauth
User = get_user_model()

class ModelOfAuto(models.Model):
    title = models.CharField("Модель автомобиля", max_length=100)

    class Meta:
        verbose_name="Модель автомобиля"
        verbose_name_plural="Модель автомобиля"

    def __str__(self):
        return self.title

class MarkOfAuto(models.Model):
    title = models.CharField("Марка автомобиля", max_length=100)

    class Meta:
        verbose_name="Марка автомобиля"
        verbose_name_plural="Марка автомобиля"

    def __str__(self):
        return self.title

class BodyTypeOfAuto(models.Model):
    title = models.CharField("Кузов автомобиля", max_length=100)

    class Meta:
        verbose_name="Кузов автомобиля"
        verbose_name_plural="Кузов автомобиля"

    def __str__(self):
        return self.title

class ColorOfAuto(models.Model):
    title = models.CharField("Цвет автомобиля", max_length=100)

    class Meta:
        verbose_name="Цвет автомобиля"
        verbose_name_plural="Цвет автомобиля"

    def __str__(self):
        return self.title

class TransmissionTypeOfAuto(models.Model):
    title = models.CharField("Тип коробки передач автомобиля", max_length=100)

    class Meta:
        verbose_name="Тип коробки передач автомобиля"
        verbose_name_plural="Тип коробки передач автомобиля"

    def __str__(self):
        return self.title

class DriveUnitOfAuto(models.Model):
    title = models.CharField("Привод автомобиля", max_length=100)

    class Meta:
        verbose_name="Привод автомобиля"
        verbose_name_plural="Привод автомобиля"

    def __str__(self):
        return self.title

class AvitoObject(models.Model):
    linkOnAd = models.CharField("Ссылка на объявление", max_length=1500, null=True, blank=True)
    AdName = models.CharField("Название объявления", max_length=100, null=True, blank=True)

    MarkAuto = models.ForeignKey(MarkOfAuto, verbose_name="Марка автомобиля", on_delete=models.SET_NULL, null=True, blank=True)
    ModelAuto = models.ForeignKey(ModelOfAuto, verbose_name="Модель автомобиля", on_delete=models.SET_NULL, null=True, blank=True)
    Price = models.IntegerField(blank=True, null=True)
    YearOfIssue  = models.IntegerField(blank=True, null=True)
    Mileage  = models.IntegerField(blank=True, null=True)
    BodyType = models.ForeignKey(BodyTypeOfAuto, verbose_name="Тип кузова автомобиля", on_delete=models.SET_NULL, null=True, blank=True)
    Color = models.ForeignKey(ColorOfAuto, verbose_name="Цвет автомобиля", on_delete=models.SET_NULL, null=True, blank=True)
    EngineCapacity = models.FloatField(blank=True, null=True)
    TransmissionType = models.ForeignKey(TransmissionTypeOfAuto, verbose_name="Тип коробки передач", on_delete=models.SET_NULL, null=True, blank=True)
    DriveUnit = models.ForeignKey(DriveUnitOfAuto, verbose_name="Привод", on_delete=models.SET_NULL, null=True, blank=True)
    NumberOfOwners = models.IntegerField(blank=True, null=True)
    EnginePower = models.IntegerField(blank=True, null=True)
    Description = models.TextField(blank=True, null=True)
    Picture = models.CharField("Ссылка на изображение", max_length=1500, null=True, blank=True)

    class Meta:
        verbose_name="Авито"
        verbose_name_plural="Авито"

    def __str__(self):
        return self.AdName

class DromObject(models.Model):
    linkOnAd = models.CharField("Ссылка на объявление", max_length=1500, null=True, blank=True)
    AdName = models.CharField("Название объявления", max_length=100, null=True, blank=True)

    MarkAuto = models.ForeignKey(MarkOfAuto, verbose_name="Марка автомобиля", on_delete=models.SET_NULL, null=True, blank=True)
    ModelAuto = models.ForeignKey(ModelOfAuto, verbose_name="Модель автомобиля", on_delete=models.SET_NULL, null=True, blank=True)
    YearOfIssue  = models.IntegerField(blank=True, null=True)
    Color = models.ForeignKey(ColorOfAuto, verbose_name="Цвет автомобиля", on_delete=models.SET_NULL, null=True, blank=True)
    Mileage  = models.IntegerField(blank=True, null=True)
    Price = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name="Дром"
        verbose_name_plural="Дром"

    def __str__(self):
        return self.AdName


class AMruObject(models.Model):
    linkOnAd = models.CharField("Ссылка на объявление", max_length=1500, null=True, blank=True)
    AdName = models.CharField("Название объявления", max_length=100, null=True, blank=True)

    MarkAuto = models.ForeignKey(MarkOfAuto, verbose_name="Марка автомобиля", on_delete=models.SET_NULL, null=True, blank=True)
    ModelAuto = models.ForeignKey(ModelOfAuto, verbose_name="Модель автомобиля", on_delete=models.SET_NULL, null=True, blank=True)
    YearOfIssue  = models.IntegerField(blank=True, null=True)
    Color = models.ForeignKey(ColorOfAuto, verbose_name="Цвет автомобиля", on_delete=models.SET_NULL, null=True, blank=True)
    Mileage  = models.IntegerField(blank=True, null=True)
    Price = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name="АМру"
        verbose_name_plural="АМру"

    def __str__(self):
        return self.AdName

class YoulaObject(models.Model):
    linkOnAd = models.CharField("Ссылка на объявление", max_length=1500, null=True, blank=True)
    AdName = models.CharField("Название объявления", max_length=100, null=True, blank=True)

    MarkAuto = models.ForeignKey(MarkOfAuto, verbose_name="Марка автомобиля", on_delete=models.SET_NULL, null=True, blank=True)
    ModelAuto = models.ForeignKey(ModelOfAuto, verbose_name="Модель автомобиля", on_delete=models.SET_NULL, null=True, blank=True)
    YearOfIssue  = models.IntegerField(blank=True, null=True)
    Color = models.ForeignKey(ColorOfAuto, verbose_name="Цвет автомобиля", on_delete=models.SET_NULL, null=True, blank=True)
    Mileage  = models.IntegerField(blank=True, null=True)
    Price = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name="Юла"
        verbose_name_plural="Юла"

    def __str__(self):
        return self.AdName

class MainAdObject(models.Model):
    AdName = models.CharField("Название объявления", max_length=100, null=True, blank=True)

    Avito = models.ForeignKey(AvitoObject, verbose_name="Авито", blank=True, on_delete=models.SET_NULL, null=True)
    Drom = models.ForeignKey(DromObject, verbose_name="Дром", blank=True, on_delete=models.SET_NULL, null=True)
    AMru = models.ForeignKey(AMruObject, verbose_name="АМру", blank=True, on_delete=models.SET_NULL, null=True)
    Youla = models.ForeignKey(YoulaObject, verbose_name="Юла", blank=True, on_delete=models.SET_NULL, null=True)

    MarkAuto = models.ForeignKey(MarkOfAuto, verbose_name="Марка автомобиля", on_delete=models.SET_NULL, null=True, blank=True)
    ModelAuto = models.ForeignKey(ModelOfAuto, verbose_name="Модель автомобиля", on_delete=models.SET_NULL, null=True, blank=True)
    Price = models.IntegerField(blank=True, null=True)
    YearOfIssue  = models.IntegerField(blank=True, null=True)
    Mileage  = models.IntegerField(blank=True, null=True)
    BodyType = models.ForeignKey(BodyTypeOfAuto, verbose_name="Тип кузова автомобиля", on_delete=models.SET_NULL, null=True, blank=True)
    Color = models.ForeignKey(ColorOfAuto, verbose_name="Цвет автомобиля", on_delete=models.SET_NULL, null=True, blank=True)
    EngineCapacity = models.FloatField(blank=True, null=True)
    TransmissionType = models.ForeignKey(TransmissionTypeOfAuto, verbose_name="Тип коробки передач", on_delete=models.SET_NULL, null=True, blank=True)
    DriveUnit = models.ForeignKey(DriveUnitOfAuto, verbose_name="Привод", on_delete=models.SET_NULL, null=True, blank=True)
    NumberOfOwners = models.IntegerField(blank=True, null=True)
    EnginePower = models.IntegerField(blank=True, null=True)
    Description = models.TextField(blank=True, null=True)
    minDescription = models.CharField("Описание", max_length=500, blank=True, null=True)
    Picture = models.CharField("Ссылка на изображение", max_length=1500, null=True, blank=True)

    class Meta:
        verbose_name="Объявление"
        verbose_name_plural="Объявления"

    def __str__(self):
        return self.AdName




class Comments(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.SET_NULL, null=True, blank=True)
    ad = models.ForeignKey(
        MainAdObject,
        verbose_name="Комментируемое Объявление",
        on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField("Текст комментария", blank=True, null=True)
    created = models.DateTimeField("Дата добавления комментария", auto_now_add=True, null=True, blank=True)
    class Meta:
        verbose_name="Комментарий"
        verbose_name_plural="Комментарии"

    def __str__(self):
        return "{}".format(self.user)
