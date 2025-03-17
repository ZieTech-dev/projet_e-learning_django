from django import forms
from .models import ChatMessage, ForumMessage, GroupeMessage

class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['contenu']
        widgets = {
            'contenu': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Écrivez votre message ici...'})
        }

class ForumMessageForm(forms.ModelForm):
    class Meta:
        model = ForumMessage
        fields = ['contenu']
        widgets = {
            'contenu': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Écrivez votre message ici...'})
        }

class GroupeMessageForm(forms.ModelForm):
    class Meta:
        model = GroupeMessage
        fields = ['contenu']
        widgets = {
            'contenu': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Écrivez votre message ici...'})
        }
