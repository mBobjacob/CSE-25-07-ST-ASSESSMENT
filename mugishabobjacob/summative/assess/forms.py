from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Users

class UserForm(UserCreationForm):
    class Meta():
        model = Users
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        username = forms.CharField(error_messages = {"required": "Please Enter the Username"})
        email = forms.EmailField(error_messages = {"required": "Please Enter the email"})
        password1 = forms.CharField(error_messages = {"required": "Please Enter the password"})
        password2 = forms.CharField(error_messages = {"required": "Please Enter the password"})

class UserAuthenticationForm(AuthenticationForm):
    error_messages = {
        "invalid login": "Hello, Please cyeck your credentails and try again"
    }
    username = forms.CharField(error_messages = {"required": "Please Enter the Username"})
    password1 = forms.CharField(error_messages = {"required": "Please Enter the password"})
