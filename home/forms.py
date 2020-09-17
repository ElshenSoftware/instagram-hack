from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email','parol','ad']
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'emailunvaniniz@gmail.com'}),
            'parol': forms.TextInput(attrs={'placeholder': '***********'}),
            'ad': forms.TextInput(attrs={'placeholder': '@'}),
        }
