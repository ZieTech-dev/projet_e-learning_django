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


class Forum(models.Model):
    class Meta:
        verbose_name="Forum"
        verbose_name_plural="Forums"

    titre = models.CharField(max_length=200)
    description = models.TextField()
    messages = models.ForeignKey("discussion.Message", on_delete=models.CASCADE, related_name="Message_Forum_id")
    participants_id = models.ManyToManyField(User,related_name="Participant_Forum_ids")


class Chat (models.Model):
    class Meta:
        verbose_name="Chat"
        verbose_name_plural="Chats"

    nomChat = models.CharField(max_length=200)
    typeChat = models.CharField(max_length=200)
    messages = models.ForeignKey("discussion.Message", on_delete=models.CASCADE, related_name="Message_Chat_id")
    participants_id = models.ManyToManyField(User, related_name="Participant_Chat_ids")


class ForumCours(Forum):
    pass