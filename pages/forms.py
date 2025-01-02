from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name")
    email = forms.EmailField(label="Email")
    phone_number = forms.CharField(label="phone_number")
    message = forms.CharField(widget=forms.Textarea, label="Message")




