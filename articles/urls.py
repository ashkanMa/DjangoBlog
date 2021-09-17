from django.urls import path
from . import views
from . import views

urlpatterns = [
    path('', views.article_list, name="all_article"),
    path('/<slug:slug>', views.article_detail, name="article_detail"),
]
