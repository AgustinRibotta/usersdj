# Django
from django import forms
from django.contrib.auth import authenticate
# Models
from .models import User



# User Register
class UserRegisterForm(forms.ModelForm):
    """Form definition for User."""

    password1 = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Password'
            }
        )
    )
    password2 = forms.CharField(
        label='Confirm Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Re Enter Password'
            }
        )
    )


    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = (
            'username',
            'email',
            'name',
            'last_name',
            'gender',

        )
        widgets = {
           'username': forms.TextInput(
                attrs={
                    'placeholder' : 'Username'
                }
            ),
           'email': forms.TextInput(
                attrs={
                    'placeholder' : 'Email'
                }
            ),
           'name': forms.TextInput(
                attrs={
                    'placeholder' : 'Fisrt Name'
                }
            )
        }
        
    def clean_password2 (self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Passwords do not match')
        elif len(self.cleaned_data['password1']) < 5:
            self.add_error('password2', 'The password is too short it must have more than 5 characters')
                
                
# Login
class LoginForm(forms.Form):

    username = forms.CharField(
        label='Username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'Username'
            }
        )
    )
    password1 = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Password'
            }
        )
    )
    
    def clean(self):
        cleane_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password1']
        
        if not authenticate(username=username, password=password):
            raise forms.ValidationError('The data entered is not correct')
        
        return self.cleaned_data
    
   
# Update Password User 
class UpdatePasswordForm(forms.Form):
    
    password1 = forms.CharField(
        label='Current password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Current password'
            }
        )
    )
    password2 = forms.CharField(
        label='Nwe Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Nwe Password'
            }
        )
    )
    password3 = forms.CharField(
        label='Repeat new password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Repeat new password'
            }
        )
    )
        
    def clean_password3 (self):
        if self.cleaned_data['password2'] != self.cleaned_data['password3']:
            self.add_error('password3', 'Passwords do not match')
        elif len(self.cleaned_data['password2']) < 5:
            self.add_error('password3', 'The password is too short it must have more than 5 characters')
       

class VerificationForm(forms.Form):
    cod_register = forms.CharField( required= True)
    

    def __init__(self, pk, *args, **kwargs):
        self.id_user = pk
        super(VerificationForm, self).__init__(*args, **kwargs)
    
    
    def clean_cod_register(self):
        code = self.cleaned_data['cod_register']
        
        if len(code) == 6:
            # Verificacxion de codio e id de user
            activo = User.objects.cod_validate(
                self.id_user ,
                code,
            )
            if not activo:
                raise forms.ValidationError('The data entered is not correct')
        else:
            raise forms.ValidationError('The data entered is not correct')