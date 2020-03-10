from django.urls import path
from . import views


urlpatterns = [

    path('',views.listas,name='listas'),
    path('lista2020',views.series2020,name='series2020'),
    path('lista2019',views.series2019,name='series2019'),
    path('lista2018',views.series2018,name='series2018'),
    path('new', views.serie_new, name='serie_new'),
    path('<str:serie>/edit/', views.serie_edit, name='serie_edit'),

    ]
