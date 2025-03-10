from django.contrib import admin
from .models import Nature, Facture, RapportFinancier, Compte, Paiement
from account.models import Comptable

# Personnalisation du modèle Nature dans l'admin
class NatureAdmin(admin.ModelAdmin):
    list_display = ('titre', 'statut', 'created_at', 'last_updated_at')
    list_filter = ('statut', 'created_at')
    search_fields = ('titre',)
    ordering = ('-created_at',)

# Personnalisation du modèle Facture dans l'admin
class FactureAdmin(admin.ModelAdmin):
    list_display = ('titre', 'montant', 'statut', 'created_at', 'last_updated_at')
    list_filter = ('statut', 'created_at')
    search_fields = ('titre',)
    ordering = ('-created_at',)

# Personnalisation du modèle RapportFinancier dans l'admin
class RapportFinancierAdmin(admin.ModelAdmin):
    list_display = ('titre', 'RevenusTotaux', 'depensesTotales', 'statut', 'created_at', 'last_updated_at')
    list_filter = ('statut', 'created_at')
    search_fields = ('titre',)
    ordering = ('-created_at',)

# Personnalisation du modèle Compte dans l'admin
class CompteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'operateur', 'type', 'numero_compte', 'statut', 'created_at', 'last_updated_at')
    list_filter = ('statut', 'created_at', 'operateur')
    search_fields = ('nom', 'numero_compte')
    ordering = ('-created_at',)

# Personnalisation du modèle Paiement dans l'admin
class PaiementAdmin(admin.ModelAdmin):
    list_display = ('montant', 'type', 'comptable', 'compte', 'facture', 'nature', 'rapportFinancier', 'statut', 'created_at', 'last_updated_at')
    list_filter = ('statut', 'created_at', 'comptable', 'compte', 'facture', 'nature', 'rapportFinancier')
    search_fields = ('montant', 'type', 'comptable__username', 'compte__numero_compte')
    ordering = ('-created_at',)

# Enregistrer les modèles avec leurs personnalisations
admin.site.register(Nature, NatureAdmin)
admin.site.register(Facture, FactureAdmin)
admin.site.register(RapportFinancier, RapportFinancierAdmin)
admin.site.register(Compte, CompteAdmin)
admin.site.register(Paiement, PaiementAdmin)
