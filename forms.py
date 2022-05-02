from django import forms

class sign_up_form(forms.Form):
    fname=forms.CharField(label='First Name:', max_length=20)
    lname=forms.CharField(label='Last Name:', max_length=20)
    phone=forms.CharField(label='Phone:', max_length=10)
    email=forms.CharField(label='Email Address:', max_length=100)
    password=forms.CharField(label='Password:', max_length=100)
    
class log_in_form(forms.Form):
    email=forms.CharField(label='Email Address:', max_length=100)
    password=forms.CharField(label='Password:', max_length=100)
    
    