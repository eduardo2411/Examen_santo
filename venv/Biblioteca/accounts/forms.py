from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterForm(forms.Form):
    username = forms.CharField(label="Introduce tu usuario",
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Nombre'}))
    email = forms.EmailField(label="introduce tu correo electronico",
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Correo'}))
    password = forms.CharField(label="introduce tu password privada",
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Contrasenia'}))
    password2 = forms.CharField(label='Confirme su password:', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                                 'placeholder': 'Repite Contrasenia'}))

    def clean_password2(self):
        print "Entro"
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            print "que pasa"
            raise forms.ValidationError("Password debe coincidir! ")
        return password

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__icontains=username).exists():
            raise forms.ValidationError("Este usuario ya existe!")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__icontains=email).exists():
            raise forms.ValidationError("Este email ya esta registrado!")
        return email
