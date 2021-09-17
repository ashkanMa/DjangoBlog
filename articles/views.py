from django.shortcuts import render
from . import models


# Create your views here.

def article_list(request):
    articles = models.Article.objects.all().order_by('date')
    args = {'articles': articles}
    return render(request, 'articles/article_list.html', args)
