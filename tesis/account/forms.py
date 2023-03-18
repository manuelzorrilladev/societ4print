from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import CustomUser

CAMPOS = ("username","first_name","last_name","email","age","phone")

class CustomUserCreationForm(UserCreationForm):

    class Meta():
        model = CustomUser
        fields = CAMPOS
        labels = {
            "age": 'Edad',
            "phone":'Telefono'
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta():
        model = CustomUser
        fields = ("username","first_name","last_name","email","phone")
  

# Permision

class AddPermission(forms.ModelForm):
    class Meta():
        model = CustomUser
        fields = {'is_staff'}
        
