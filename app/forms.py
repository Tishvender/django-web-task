from django import forms  
from .models import Employee
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = ['name','contact','email_department'] 
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'contact' : forms.NumberInput (attrs={'class':'form-control'}),
            'email_department' : forms.EmailInput(attrs={'class':'form-control'}),
        }

class SignupForm(UserCreationForm):
    password2 =  forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class  Meta:
        model = User
        fields = ['username', 'first_name','last_name','email']
        labels = {'email':'Email'}