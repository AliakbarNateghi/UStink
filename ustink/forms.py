from django import forms
from ustink.models import message


class homeForm(forms.Form):
    name = forms.CharField(label='اسمش چیه?', max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control persian-font',
                                                         'placeholder': 'علی اکبر'
                                                         }))

    email = forms.EmailField(label='ایمیلش چیه?', max_length=256,
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'ustink@gmail.com'
                                                           }))


class loginForm(forms.Form):
    userName = forms.CharField(label='نام کاربری', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'}))
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class registerForm(forms.Form):
    userName = forms.CharField(label='نام کاربری', max_length=100)
    email = forms.EmailField(label='ایمیل', max_length=256)
    password1 = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)
    password2 = forms.CharField(label='تکراز رمز عبور', widget=forms.PasswordInput)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
