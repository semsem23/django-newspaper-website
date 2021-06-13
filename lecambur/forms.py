

from django import forms

class ContactForm(forms.Form):
    
    name = forms.CharField(max_length=80, label="Nom", widget=forms.TextInput(attrs={'class': 'input[type=text]'}))
    subject = forms.CharField(max_length=100, label="Objet", widget=forms.TextInput(attrs={'class': 'input[type=text]'}))
    sender = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class': 'input[type=email]'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Veuillez saisir votre message'}))


   