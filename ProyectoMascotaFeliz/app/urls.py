from django.urls import path 
from .views import home, somos, register, galeria, feriados

urlpatterns=[
    path('', home, name="home"),
    path('somos/', somos, name= "somos"),
    path('register/', register, name="register"),
    path('galeria/', galeria, name="galeria"),
    path('feriados/', feriados, name="feriados"),

]