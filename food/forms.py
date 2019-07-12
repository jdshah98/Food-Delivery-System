from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    email = forms.CharField(max_length=254, widget=forms.HiddenInput(), required=False)
    subject = forms.CharField(max_length=50, required=True)
    message = forms.CharField(max_length=500, required=True, widget=forms.Textarea(attrs={'rows': '3'}))
    user = forms.CharField(max_length=50, widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Feedback
        fields = ['email','subject','message','user']