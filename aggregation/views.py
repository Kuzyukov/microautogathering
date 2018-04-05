from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from aggregation.models import MainAdObject, Comments
from aggregation.forms import CommentForm

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
    comment = Comments.objects.filter(ad=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.user = request.user
            form.ad = ad
            form.save()
            return redirect(objectPage, pk)
    else:
        form = CommentForm()

    return render(request, 'aggregation/objectPage.html', {"ad": ad, "comments": comment, "form": form})
