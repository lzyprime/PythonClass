from django.shortcuts import render

from .models import Artice

def index(request):
    articles = Artice.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})

def article_page(request, article_id):
    article = Artice.objects.get(pk = article_id)
    return render(request, 'blog/articlePage.html', {'article' : article})