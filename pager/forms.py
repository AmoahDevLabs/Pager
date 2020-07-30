from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Enter your name')
    email = forms.EmailField(required=False, label='Enter your e-mail address')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
