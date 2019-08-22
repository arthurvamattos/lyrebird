from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resultados/', views.ResultsView.as_view(), name='resultados'),
    path('inclusao/', views.solicitacao_inclusao, name='solicita_inclusao'),
]
