from django.shortcuts import render

def agregationPage(request):
    return render(request, 'aggregation/aggregationPage.html')
