from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainPage, name = "mainPage"),
    path('aggregation/', views.agregationPage, name = "agregationPage"),
    path('about/', views.aboutPage, name = "aboutPage"),
    path('main/', views.mainPage, name = "mainPage"),
    path('statistic/', views.statisticPage, name = "statisticPage"),
    path('forum/', views.forumPage, name = "forumPage"),
    path('login/', views.loginPage, name = "loginPage"),
    path('object/<int:pk>', views.objectPage, name = "objectPage"),
]
