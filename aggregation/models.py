from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ModelOfAuto(models.Model):
    title = models.CharField("Модель автомобиля", max_lenght=100)

    class Meta:
        verbose_name="Модель автомобиля"
        verbose_name_plural="Модель автомобиля"

    def __str__(self):
        return self.title

class MarkOfAuto(models.Model):
    title = models.CharField("Марка автомобиля", max_lenght=100)

    class Meta:
        verbose_name="Марка автомобиля"
        verbose_name_plural="Марка автомобиля"

    def __str__(self):
        return self.title

class BodyTypeOfAuto(models.Model):
    title = models.CharField("Кузов автомобиля", max_lenght=100)

    class Meta:
        verbose_name="Кузов автомобиля"
        verbose_name_plural="Кузов автомобиля"

    def __str__(self):
        return self.title

class ColorOfAuto(models.Model):
    title = models.CharField("Цвет автомобиля", max_lenght=100)

    class Meta:
        verbose_name="Цвет автомобиля"
        verbose_name_plural="Цвет автомобиля"

    def __str__(self):
        return self.title

class TransmissionTypeOfAuto(models.Model):
    title = models.CharField("Тип коробки передач автомобиля", max_lenght=100)

    class Meta:
        verbose_name="Тип коробки передач автомобиля"
        verbose_name_plural="Тип коробки передач автомобиля"

    def __str__(self):
        return self.title

class DriveUnitOfAuto(models.Model):
    title = models.CharField("Привод автомобиля", max_lenght=100)

    class Meta:
        verbose_name="Привод автомобиля"
        verbose_name_plural="Привод автомобиля"

    def __str__(self):
        return self.title

class AvitoObject(models.Model):
    linkOnAd = models.CharField("Ссылка на объявление", max_lenght=1500)
    AdName = models.CharField("Название объявления", max_lenght=100)

    MarkAuto = models.ForeignKey(MarkOfAuto, verbose_name="Марка автомобиля")
    ModelAuto = models.ForeignKey(ModelOfAuto, verbose_name="Модель автомобиля")
    Price = models.IntegerField()
    YearOfIssue  = models.IntegerField()
    Mileage  = models.IntegerField()
    BodyType = models.ForeignKey(BodyTypeOfAuto, verbose_name="Тип кузова автомобиля")
    Color = models.ForeignKey(ColorOfAuto, verbose_name="Цвет автомобиля")
    EngineCapacity = models.IntegerField()
    TransmissionType = models.ForeignKey(TransmissionTypeOfAuto, verbose_name="Тип коробки передач")
    DriveUnit = models.ForeignKey(DriveUnitOfAuto, verbose_name="Привод")
    NumberOfOwners = models.IntegerField()
    EnginePower = models.IntegerField()
    Description = models.TextField()
    Picture = models.CharField("Ссылка на изображение", max_lenght=1500)

    class Meta:
        verbose_name="Авито"
        verbose_name_plural="Авито"

    def __str__(self):
        return self.AdName

class DromObject(models.Model):
    linkOnAd = models.CharField("Ссылка на объявление", max_lenght=1500)
    AdName = models.CharField("Название объявления", max_lenght=100)

    MarkAuto = models.ForeignKey(MarkOfAuto, verbose_name="Марка автомобиля")
    ModelAuto = models.ForeignKey(ModelOfAuto, verbose_name="Модель автомобиля")
    YearOfIssue  = models.IntegerField()
    Color = models.ForeignKey(ColorOfAuto, verbose_name="Цвет автомобиля")
    Mileage  = models.IntegerField()
    Price = models.IntegerField()

    class Meta:
        verbose_name="Дром"
        verbose_name_plural="Дром"

    def __str__(self):
        return self.AdName


class AMruObject(models.Model):
    linkOnAd = models.CharField("Ссылка на объявление", max_lenght=1500)
    AdName = models.CharField("Название объявления", max_lenght=100)

    MarkAuto = models.ForeignKey(MarkOfAuto, verbose_name="Марка автомобиля")
    ModelAuto = models.ForeignKey(ModelOfAuto, verbose_name="Модель автомобиля")
    YearOfIssue  = models.IntegerField()
    Color = models.ForeignKey(ColorOfAuto, verbose_name="Цвет автомобиля")
    Mileage  = models.IntegerField()
    Price = models.IntegerField()

    class Meta:
        verbose_name="АМру"
        verbose_name_plural="АМру"

    def __str__(self):
        return self.AdName

class YoulaObject(models.Model):
    linkOnAd = models.CharField("Ссылка на объявление", max_lenght=1500)
    AdName = models.CharField("Название объявления", max_lenght=100)

    MarkAuto = models.ForeignKey(MarkOfAuto, verbose_name="Марка автомобиля")
    ModelAuto = models.ForeignKey(ModelOfAuto, verbose_name="Модель автомобиля")
    YearOfIssue  = models.IntegerField()
    Color = models.ForeignKey(ColorOfAuto, verbose_name="Цвет автомобиля")
    Mileage  = models.IntegerField()
    Price = models.IntegerField()

    class Meta:
        verbose_name="Юла"
        verbose_name_plural="Юла"

    def __str__(self):
        return self.AdName

class MainAdObject(models.Model):
    AdName = models.CharField("Название объявления", max_lenght=100)

    Avito = models.ForeignKey(AvitoObject, verbose_name="Авито")
    Drom = models.ForeignKey(DromObject, verbose_name="Дром")
    AMru = models.ForeignKey(AMruObject, verbose_name="Дром")
    Youla = models.ForeignKey(YoulaObject, verbose_name="Дром")

    MarkAuto = models.ForeignKey(MarkOfAuto, verbose_name="Марка автомобиля")
    ModelAuto = models.ForeignKey(ModelOfAuto, verbose_name="Модель автомобиля")
    Price = models.IntegerField()
    YearOfIssue  = models.IntegerField()
    Mileage  = models.IntegerField()
    BodyType = models.ForeignKey(BodyTypeOfAuto, verbose_name="Тип кузова автомобиля")
    Color = models.ForeignKey(ColorOfAuto, verbose_name="Цвет автомобиля")
    EngineCapacity = models.IntegerField()
    TransmissionType = models.ForeignKey(TransmissionTypeOfAuto, verbose_name="Тип коробки передач")
    DriveUnit = models.ForeignKey(DriveUnitOfAuto, verbose_name="Привод")
    NumberOfOwners = models.IntegerField()
    EnginePower = models.IntegerField()
    Description = models.TextField()
    Picture = models.CharField("Ссылка на изображение", max_lenght=1500)

    class Meta:
        verbose_name="Объявление"
        verbose_name_plural="Объявления"

    def __str__(self):
        return self.AdName




class Comments(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=model.CASCADE)
    ad = models.ForeignKey(
        MainAdObject,
        verbose_name="Комментируемое Объявление",
        on_delete=model.CASCADE)
    text = models.TextField("Текст комментария")
    created = models.DateTimeField("Дата добавления комментария", auto_now_add=True, null=True)
    moderation model.BooleanField(default=False)
    class Meta:
        verbose_name="Комментарий"
        verbose_name_plural="Комментарии"

    def __str__(self):
        return "{}".format(self.user)
