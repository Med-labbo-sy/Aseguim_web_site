from django import forms

class ContactForm(forms.Form):
    nom = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Votre nom'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Votre email'
    }))
    objet = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': "Objet du message"
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Votre message',
        'rows': 5
    }))

    # Champ honeypot invisible anti-bots
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput())

    def clean_honeypot(self):
        data = self.cleaned_data['honeypot']
        if data:
            raise forms.ValidationError("Bot détecté.")
        return data
