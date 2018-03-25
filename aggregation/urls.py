from django.urls import path
from . import views

urlpatterns = [
    path('aggregation/', views.agregationPage, name = "agregationPage"),
    path('about/', views.aboutPage, name = "aboutPage"),
    path('main/', views.agregationPage, name = "mainPage"),
    path('statistic/', views.statisticPage, name = "statisticPage"),
]
