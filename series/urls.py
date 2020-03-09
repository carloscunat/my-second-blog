from django.urls import path
from . import views


urlpatterns = [
    path('', views.series_list, name='series_list'),
    path('series/new', views.serie_new, name='serie_new'),
    path('series/<str:serie>/edit/', views.serie_edit, name='serie_edit')
    ]
