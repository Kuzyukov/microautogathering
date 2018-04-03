from django.contrib import admin
from aggregation.models import ModelOfAuto, MarkOfAuto, BodyTypeOfAuto, ColorOfAuto, TransmissionTypeOfAuto, DriveUnitOfAuto

admin.site.register(ModelOfAuto)
admin.site.register(MarkOfAuto)
admin.site.register(BodyTypeOfAuto)
admin.site.register(ColorOfAuto)
admin.site.register(TransmissionTypeOfAuto)
admin.site.register(DriveUnitOfAuto)
