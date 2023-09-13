from django.urls import path
from .views import home, read_excel

urlpatterns = [
    path('',home, name='home'),
    path('read',read_excel, name='read_excel')

]
