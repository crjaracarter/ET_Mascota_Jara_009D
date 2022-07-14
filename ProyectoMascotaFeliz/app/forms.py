from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Cliente, Producto 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    password1: forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2: forms.CharField(label='ConfirmaContraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','nombre', 'apellido' ,'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}


class ClienteForm(forms.ModelForm):

    class Meta:
        model= Cliente 
        fields = ['idCliente','nombreCliente', 'apellido', 'comuna', 'correo', 'telefono', 'direccion']
        labels ={
            'idCliente' : 'IdCliente',
            'nombreCliente' : 'NombreCliente',
            'apellido' : 'Apellido',
            'comuna' : 'Comuna',
            'correo' : 'Correo',
            'telefono' : 'Telefono',
            'direccion' : 'Direccion',


        }

        widgets={
            'idCliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut del cliente', 
                    'id': 'idCliente'
                }
            ), 
            'nombreCliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre del cliente', 
                    'id': 'nombreCliente'
                }
            ), 
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese apellido del cliente', 
                    'id': 'apellido'
                }
            ),
            'comuna': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese la comuna del cliente', 
                    'id': 'comuna'
                }
            ),
            'correo': forms.EmailInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingresa el correo del cliente', 
                    'id': 'correo'
                }
            ),  
            'telefono': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingresa el telefono del cliente', 
                    'id': 'telefono'
                }
            ),  
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingresa la direccion del cliente', 
                    'id': 'direccion',
                }
            )    
        }

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['idProducto', 'nombreProducto', 'descripcion', 'precioProducto' , 'stockProducto' ,'imagen' ]
        labels={'idProducto' : 'IdProducto',
                'nombreProducto' : 'NombreProducto',
                'descripcion' : 'Descripcion',
                'precioProducto' : 'PrecioProducto',
                'stockProducto' : 'StockProducto',


                'imagen' : 'Imagen',
                
        }
        
        imagen=forms.ImageField(label="Avatar",required=False,widget=forms.FileInput(attrs={'class':'form-control'}))



        widgets={
            'idProducto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese id del producto', 
                    'id': 'idProducto'
                }
            ), 
            'nombreProducto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre del producto', 
                    'id': 'nombreProducto'
                }
            ), 
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese descripcion del producto', 
                    'id': 'descripcion'
                }
            ), 
            'precioProducto': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese precio del producto', 
                    'id': 'precioProducto'
                }
            ), 
            'stockProducto': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese stock del producto', 
                    'id': 'stockProducto',
                }
            ), 
            # 'imagen': forms.ImageField(
            #     attrs={
            #         'class': 'form-control', 
            #         'placeholder': 'Ingrese imagen del producto', 
            #         'id': 'imagen'
            #     }
            # ),

         }

       
        
        
        
        
 