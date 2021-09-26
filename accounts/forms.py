from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User



class register_form(ModelForm):
    c_password= forms.CharField(max_length= 50, widget= forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']

class login_form(forms.Form):
    username = forms.CharField(max_length= 100)
    password = forms.CharField(max_length= 100, widget = forms.PasswordInput())
    
    class Meta:
        fields = ['username', 'password']
