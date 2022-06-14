from django.urls import path 
from .views import form_mod_cli, home, somos, register, galeria, feriados, mostrar_producto, form_crear_producto, form_crear_cliente, form_mod_prod, form_del_producto, form_mod_cli, form_del_cliente
urlpatterns=[
    path('', home, name="home"),
    path('somos/', somos, name= "somos"),
    path('register/', register, name="register"),
    path('galeria/', galeria, name="galeria"),
    path('feriados/', feriados, name="feriados"),
    path('producto/', mostrar_producto,name="producto"),
    path('form_crear_producto/', form_crear_producto,name="form_crear_producto"),
    path('form_crear_cliente/', form_crear_cliente,name="form_crear_cliente"),
    path('form_mod_prod<id>', form_mod_prod, name="form_mod_prod"),
    path('form_del_producto<id>', form_del_producto, name="form_del_producto"),
    path('form_mod_cli<id>', form_mod_cli, name="form_mod_cli"),
    path('form_del_cliente<id>', form_del_cliente, name="form_del_cliente"),
]