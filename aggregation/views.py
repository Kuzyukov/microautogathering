from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from aggregation.models import MainAdObject

def agregationPage(request):
    #вывод всех объявлений
    ads_list = MainAdObject.objects.all()
    paginator = Paginator(ads_list, 15)# Show 15 contacts per page
    page = request.GET.get('page')
    ads = paginator.get_page(page)
    return render(request, 'aggregation/aggregationPage.html', {"ads": ads})

def aboutPage(request):
    return render(request, 'aggregation/aboutPage.html')

def mainPage(request):
    return render(request, 'aggregation/mainPage.html')

def statisticPage(request):
    return render(request, 'aggregation/statisticPage.html')

def forumPage(request):
    return render(request, 'aggregation/forumPage.html')

def loginPage(request):
    return render(request, 'aggregation/loginPage.html')

def objectPage(request, pk):
    #вызов статьи по prymary key
    ad = get_object_or_404(MainAdObject, id=pk)
    return render(request, 'aggregation/objectPage.html', {"ad": ad})
