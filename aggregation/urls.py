from django.urls import path
from . import views

urlpatterns = [
    path('', views.agregationPage, name = "agregationPage")
]
