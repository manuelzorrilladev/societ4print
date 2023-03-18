from django import forms


from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User




class Registro(UserCreationForm):

    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs)->None:
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for field in ['username','password1','password2']:
            self.fields[field].help_text = None
    

    class Meta():
        model = User
        fields = ['username','email','password1','password2']
        labels = {
            'username': 'Nombre',
            'email': 'Correo Electronico',
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña'
            }

