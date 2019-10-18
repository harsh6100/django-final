from django import forms  
from .models import Account 

class SignupForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = "__all__"
