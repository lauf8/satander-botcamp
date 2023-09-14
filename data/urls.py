from django.urls import path
from .views import (home, read_excel, return_excel, athlete_index,
                    sport_index, sport_detail
                    )

urlpatterns = [
    path('',home, name='home'),
    path('read',read_excel, name='read_excel'),
    path('return', return_excel,name='return_excel'),
    path('athletes',athlete_index, name= 'athlete_index'),
    path('sports',sport_index, name= 'sport_index'),
    path('sports/detail/<int:pk>',sport_detail, name= 'sport_detail'),




]
