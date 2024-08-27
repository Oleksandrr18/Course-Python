from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control bg-light border-0 px-4',
                                                             'placeholder': 'Username',
                                                             'style': 'height: 55px;'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control bg-light border-0 px-4',
                                                                 'placeholder': 'Password',
                                                                 'style': 'height: 55px;'}))



class RegisterForm(forms.ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control bg-light border-0 px-4',
                                                                                    'placeholder': 'Password',
                                                                                    'style': 'height: 55px;'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control bg-light border-0 px-4',
                                                                                            'placeholder': 'Confirm Password',
                                                                                            'style': 'height: 55px;'}))

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords don\'t match.')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control bg-light border-0 px-4',
                                               'placeholder': 'Username',
                                               'style': 'height: 55px;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control bg-light border-0 px-4',
                                            'placeholder': 'Email',
                                            'style': 'height: 55px;'}),
        }