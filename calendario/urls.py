from django.urls import path, include
from . import views

app_name = 'calendario'
urlpatterns = [

    path('calendario/', views.CalendarView, name='calendario'),
]
