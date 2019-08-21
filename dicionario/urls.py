from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resultados/', views.resultados, name='resultados'),
    path('pedido/', views.pedido_inclusao, name='pedido_inclusao'),
]
