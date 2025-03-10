from django.contrib import admin
from .models import Message, Forum, Chat, ForumCours, Groupe

# Personnalisation du modèle Message dans l'admin
class MessageAdmin(admin.ModelAdmin):
    list_display = ('contenu', 'dateEnvoi', 'auteur_id', 'statut', 'created_at', 'last_updated_at')
    list_filter = ('statut', 'dateEnvoi')
    search_fields = ('contenu', 'auteur_id__username')
    ordering = ('-dateEnvoi',)

# Personnalisation du modèle Forum dans l'admin
class ForumAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description', 'statut', 'created_at', 'last_updated_at')
    list_filter = ('statut', 'created_at')
    search_fields = ('titre', 'description')
    ordering = ('-created_at',)

# Personnalisation du modèle Chat dans l'admin
class ChatAdmin(admin.ModelAdmin):
    list_display = ('nomChat', 'typeChat', 'statut', 'created_at', 'last_updated_at')
    list_filter = ('statut', 'created_at')
    search_fields = ('nomChat', 'typeChat')
    ordering = ('-created_at',)

# Personnalisation du modèle ForumCours dans l'admin
class ForumCoursAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description', 'statut', 'created_at', 'last_updated_at')
    list_filter = ('statut', 'created_at')
    search_fields = ('titre', 'description')
    ordering = ('-created_at',)

# Personnalisation du modèle Groupe dans l'admin
class GroupeAdmin(admin.ModelAdmin):
    list_display = ('nomGroupe', 'typeGroupe', 'statut', 'created_at', 'last_updated_at')
    list_filter = ('statut', 'created_at')
    search_fields = ('nomGroupe', 'typeGroupe')
    ordering = ('-created_at',)

# Enregistrer les modèles avec leurs personnalisations
admin.site.register(Message, MessageAdmin)
admin.site.register(Forum, ForumAdmin)
admin.site.register(Chat, ChatAdmin)
admin.site.register(ForumCours, ForumCoursAdmin)
admin.site.register(Groupe, GroupeAdmin)
