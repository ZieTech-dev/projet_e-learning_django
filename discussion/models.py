from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Message(models.Model):
    class Meta:
        verbose_name="Message"
        verbose_name_plural="Messages"


    contenu = models.TextField()
    dateEnvoi = models.DateTimeField(auto_now_add=True)
    auteur_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auteur_Message_ids")

    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)


class Forum(models.Model):
    class Meta:
        verbose_name="Forum"
        verbose_name_plural="Forums"

    titre = models.CharField(max_length=200)
    description = models.TextField()
    messages = models.ForeignKey("discussion.Message", on_delete=models.CASCADE, related_name="Message_Forum_id")
    participants_id = models.ManyToManyField(User,related_name="Participant_Forum_ids")

    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)


class Chat (models.Model):
    class Meta:
        verbose_name="Chat"
        verbose_name_plural="Chats"

    nomChat = models.CharField(max_length=200)
    typeChat = models.CharField(max_length=200)
    messages = models.ForeignKey("discussion.Message", on_delete=models.CASCADE, related_name="Message_Chat_id")
    participants_id = models.ManyToManyField(User, related_name="Participant_Chat_ids")

    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)


class ForumCours(Forum):
    pass


class Groupe(models.Model):
    class Meta:
        verbose_name="Groupe"
        verbose_name_plural="Groupes"  
    nomGroupe = models.CharField(max_length=200)
    typeGroupe = models.CharField(max_length=200)
    auteur_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Groupe_Auteur_id")
    participants_id = models.ManyToManyField("account.Enseignant", related_name="Participant_Groupe_ids")

    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)