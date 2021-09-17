from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='homePage'),
    path('about', views.about, name='aboutPage'),
    path('articles', include('articles.urls'), name='articlesListPage')
]
