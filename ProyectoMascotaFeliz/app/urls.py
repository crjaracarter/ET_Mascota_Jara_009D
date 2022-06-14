from django.urls import path 
from .views import home, somos, login, galeria, feriados

urlpatterns=[
    path('', home, name="home"),
    path('somos/', somos, name= "somos"),
    path('login/', login, name="login"),
    path('galeria/', galeria, name="galeria"),
    path('feriados/', feriados, name="feriados"),

]