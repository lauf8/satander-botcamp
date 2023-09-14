from django.urls import path
from .views import home, read_excel, return_excel

urlpatterns = [
    path('',home, name='home'),
    path('read',read_excel, name='read_excel'),
    path('return', return_excel,name='return_excel')

]
