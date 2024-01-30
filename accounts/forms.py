from django import forms
from accounts.models import profileModel
from django.contrib.auth.models import User




class ProfileRegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'First name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'Last name'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control",'placeholder':'Password'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control",'placeholder':'Email'}))

    class Meta:
        model = profileModel
        fields = ["ProfileImage", "Gender"]

    def clean_username(self):
        username1 = self.cleaned_data['username']
        if User.objects.filter(username = username1).exists():
            raise forms.ValidationError(f"{username1} this username has been taken before")
        return username1


