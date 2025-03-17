from django import forms
from .models import Payment, Message

# Formulaire pour le paiement d'une facture
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['payment_method', 'transaction_id']
        widgets = {
            'payment_method': forms.Select(choices=[
                ('card', 'Carte bancaire'),
                ('transfer', 'Virement bancaire'),
                ('cheque', 'Chèque'),
            ]),
            'transaction_id': forms.TextInput(attrs={'placeholder': 'ID de transaction (optionnel)'}),
        }

# Formulaire pour ajouter un message dans une discussion
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Votre message...'}),
        }