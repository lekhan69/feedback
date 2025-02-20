# forms.py
from django import forms
from .models import Feedback
import re

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'subject', 'message']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@example.com'):
            raise forms.ValidationError('Only @example.com emails are allowed.')
        return email
    
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 50:
            raise forms.ValidationError('Message must be at least 50 characters long.')
        return message
