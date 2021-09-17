from django.shortcuts import render, HttpResponse
from . import models


# Create your views here.

def article_list(request):
    articles = models.Article.objects.all().order_by('-date')
    args = {'articles': articles}
    return render(request, 'articles/article_list.html', args)


def article_detail(request, slug):
    article = models.Article.objects.get(slug=slug)
    args = {'article': article}
    return render(request, 'articles/article_detail.html', args)
