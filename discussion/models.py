from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Base Message Model
class Message(models.Model):
    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    contenu = models.TextField()
    dateEnvoi = models.DateTimeField(auto_now_add=True)
    auteur_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auteur_Message_ids")
    
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.auteur_id.username}: {self.contenu[:20]}"

# Forum Message
class ForumMessage(Message):
    forum = models.ForeignKey("discussion.Forum", on_delete=models.CASCADE, related_name="forum_messages")

    def __str__(self):
        return f"Forum Message from {self.auteur_id.username}"



# Chat Message
class ChatMessage(Message):
    chat = models.ForeignKey("discussion.Chat", on_delete=models.CASCADE, related_name="chat_messages")

    def __str__(self):
        return f"Chat Message from {self.auteur_id.username}"

# Groupe Message
class GroupeMessage(Message):
    groupe = models.ForeignKey("discussion.Groupe", on_delete=models.CASCADE, related_name="groupe_messages")

    def __str__(self):
        return f"Groupe Message from {self.auteur_id.username}"

# Forum Model
class Forum(models.Model):
    class Meta:
        verbose_name = "Forum"
        verbose_name_plural = "Forums"

    titre = models.CharField(max_length=200)
    description = models.TextField()
    participants_id = models.ManyToManyField(User, related_name="Participant_Forum_ids")

    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre


class ForumCours(Forum):
    # Additional fields specific to ForumCours can be added here
    def __str__(self):
        return self.titre
# Chat Model
class Chat(models.Model):
    class Meta:
        verbose_name = "Chat"
        verbose_name_plural = "Chats"

    nomChat = models.CharField(max_length=200)
    typeChat = models.CharField(max_length=200)
    participants_id = models.ManyToManyField(User, related_name="Participant_Chat_ids")

    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nomChat

# Groupe Model
class Groupe(models.Model):
    class Meta:
        verbose_name = "Groupe"
        verbose_name_plural = "Groupes"  

    nomGroupe = models.CharField(max_length=200)
    typeGroupe = models.CharField(max_length=200)
    auteur_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Groupe_Auteur_id")
    participants_id = models.ManyToManyField(User, related_name="Participant_Groupe_ids")

    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nomGroupe
