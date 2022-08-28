from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(max_length=256,
                             widget=forms.EmailInput(attrs={'placeholder': 'ustink@gmail.com', 'size': "40",
                                                            'class': "form-control form-control-lg"}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control form-control-lg",
                'placeholder': 'ali_akbar'
            }),
            'password1': PasswordInput(attrs={
                'class': "form-control form-control-lg",
                'placeholder': '**********',
            }),
            'password2': PasswordInput(attrs={
                'class': "form-control form-control-lg",
                'placeholder': '**********'
            })
        }

# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django.forms import TextInput, PasswordInput
#
#
# class CreateUserForm(forms.Form):
#     username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
#         'class': "form-control form-control-lg",
#         'placeholder': 'ali_akbar'
#     }))
#
#     email = forms.EmailField(max_length=256,
#                              widget=forms.EmailInput(attrs={'placeholder': 'ustink@gmail.com', 'size': "40",
#                                                             'class': "form-control form-control-lg"}))
#
#     password1 = forms.CharField(widget=PasswordInput(attrs={
#         'class': "form-control form-control-lg",
#         'placeholder': '**********'
#     }))
#
#     password2 = forms.CharField(widget=PasswordInput(attrs={
#         'class': "form-control form-control-lg",
#         'placeholder': '**********'
#     }))
#
#     def clean(self):
#         cleaned_data = super(CreateUserForm, self).clean()
#         password1 = cleaned_data.get("password1")
#         password2 = cleaned_data.get("password2")
#
#         if password1 != password2:
#             raise forms.ValidationError(
#                 " تایید رمز با رمز اصلی مطابقت ندارد "
#             )
