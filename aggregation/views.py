from django.shortcuts import render

def agregationPage(request):
    return render(request, 'aggregation/aggregationPage.html')

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

def objectPage(request):
    return render(request, 'aggregation/objectPage.html')
