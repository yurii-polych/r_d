from django import forms
from user.models import User


class UserCreateForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput)
    last_name = forms.CharField(widget=forms.TextInput)
    age = forms.CharField(widget=forms.NumberInput)

    class Meta:
        model = User
        fields = '__all__'
