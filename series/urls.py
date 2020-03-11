from django.urls import path, include
from . import views


urlpatterns = [

    path('',views.listas,name='listas'),
    path('listas/lista2020',views.series2020,name='series2020'),
    path('listas/lista2019',views.series2019,name='series2019'),
    path('listas/lista2018',views.series2018,name='series2018'),
    path('new_serie', views.serie_new, name='serie_new'),
    path('edit_serie/<str:serie>+<str:visto>/', views.serie_edit, name='serie_edit'),
    path('accounts/register', views.RegisterView,name='register'),
    path('', include('calendario.urls')),
    ]
