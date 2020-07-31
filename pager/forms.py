from django import forms


class ContactForm(forms.Form):
<<<<<<< HEAD
    your_name = forms.CharField(max_length=100, label='Your name')
    email = forms.CharField(required=False, max_length=100,
                            label='Your e-mail address')
=======
    name = forms.CharField(max_length=100, label='Enter your name')
    email = forms.EmailField(required=False, label='Enter your e-mail address')
>>>>>>> b1abfc4bea14afd7c1e982562f2192b2c099a91a
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
