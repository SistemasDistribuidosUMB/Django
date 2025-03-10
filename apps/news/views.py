from django.shortcuts import render

# Create your views here.
from .models import News

def news(request):
        my_news = News.objects.all()
        return render (request,"pages/news.html",{"news":my_news})