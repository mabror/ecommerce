from django import forms
from django.contrib.auth.models import User


class RegisterForms(forms.ModelForm):
    def save(self, commit=True):
        user = super(RegisterForms, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('first_name', 'username', 'password')


class LoginForms(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
