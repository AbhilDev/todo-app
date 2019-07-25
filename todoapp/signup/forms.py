from django import forms

class SignupForm(forms.Form):
    name = forms.CharField(label='your name')
    userName = forms.CharField(label='user name')
    email = forms.EmailField(label='email')
    mobile_num = forms.IntegerField(label='mobile number')