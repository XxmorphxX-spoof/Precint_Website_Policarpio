# police_app/forms.py
from django import forms
from .models import ContactInquiry

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInquiry
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'IDENTIFY YOURSELF'}),
            'email': forms.EmailInput(attrs={'placeholder': 'RETURN ADDRESS'}),
            'subject': forms.TextInput(attrs={'placeholder': 'NATURE OF INQUIRY'}),
            'message': forms.Textarea(attrs={'rows': 5, 'placeholder': 'ENTER MESSAGE CONTENT...'}),
        }