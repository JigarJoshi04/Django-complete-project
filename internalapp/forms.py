from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models


# # class SignUpForm(UserCreationForm):
# class LoginForm(forms.Form):
#     # email = forms.EmailField(max_length=150, help_text='Email')
#     # password = forms.CharField()
    
#     class Meta:
#         model = Profile
#         fields = ('email','password')





class LoginForm(forms.Form):
        class Meta:
                model=models.Profile2
                fields= ['email','password']

class SignUpForm(forms.Form):
    # first_name = forms.CharField(max_length=100, help_text='First Name')
    # last_name = forms.CharField(max_length=100, help_text='Last Name')
    # username = forms.CharField(max_length=100, help_text='Unique')
    # phone_no = forms.CharField()
    # email = forms.CharField(max_length=150, help_text='Email')
    # gst = forms.CharField()
    # aadhar = forms.CharField()
    # pan = forms.CharField()
    # password1 = forms.CharField()
    # password2 =forms.CharField()
    
    class Meta:
            model = models.Profile
            fields = ['first_name', 'last_name', 'username', 'phone_no', 'email', 'gst', 'aadhar', 'pan', 'password1',
                    'password2']
        
        # model = User
        # fields = ('first_name', 'last_name', 'username', 'phone_no', 'email', 'gst', 'aadhar', 'pan', 'password1',
        #           'password2')
