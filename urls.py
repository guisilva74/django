from django.urls import path

from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('pag02', views.pag2, name='pag_2'),
]