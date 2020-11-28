from django import forms
from .models import user_inform
from django.contrib.auth.models import User
class InfoModelForm(forms.ModelForm):
    class Meta:
        model = user_inform
        fields = ('fname','email','subject','message',)

        widgets = {
            'fname': forms.TextInput(attrs={'class': 'inputs shadow ','placeholder':'Name'}),
            'email': forms.TextInput(attrs={'class': 'inputs  shadow ','placeholder':'Email'}),
            'subject': forms.TextInput(attrs={'class': 'inputs shadow','placeholder':'Subject'}),
            'message': forms.TextInput(attrs={'class': 'resizes shadow','placeholder':'Message'})
        }
class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name","last_name","username","email","password")

        widgets = {
                'first_name':forms.TextInput(attrs={'class':'form-control'}),
                'last_name':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.TextInput(attrs={'class':'form-control'}),
                'username':forms.TextInput(attrs={'class':'form-control'}),
                'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }