from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, label= 'name', help_text='Your name', required= True)
    email = forms.EmailField(max_length=50, label= 'email', help_text='Your email', required= True)
    message = forms.CharField(max_length=400, label= 'message', help_text='Your message', required= True)