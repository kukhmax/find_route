from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={
        'class': 'form-control',                 # class bootstrap
        'placeholder': 'Input username',     # надпись внутри поля
    }))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',                 # class bootstrap
        'placeholder': 'Input password',     # надпись внутри поля
    }))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            qs = User.objects.filter(username=username)
            if not qs.exists():
                raise forms.ValidationError('User does not exist')
            if not check_password(password, qs=[0].password):
                raise forms.ValidationError('Invalid password')
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user is not active ')
        return super().clean(*args, **kwargs)