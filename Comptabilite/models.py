from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from account.models import Comptable

User = get_user_model()



class Nature(models.Model):
    class Meta:
        verbose_name = "Nature"
        verbose_name_plural = "Natures"
        

    titre = models.CharField(max_length=256)
      
    # Standards
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)


class Facture(models.Model):
    
    class Meta:
        verbose_name = "Facture"
        verbose_name_plural = "Factures"

    titre = models.CharField(max_length=256)
    montant = models.DecimalField(
        max_digits=20,
        decimal_places=5, 
        default=0.00  
    )
    
    # Standards
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)



class RapportFinancier(models.Model):
    
    class Meta:
        verbose_name = "Rapport Financier"
        verbose_name_plural = "Rapport Financiers"
        
        
    titre = models.CharField(max_length=256)
    RevenusTotaux = models.DecimalField(
        max_digits=20,
        decimal_places=5, 
        default=0.00  
    )
    depensesTotales = models.DecimalField(
        max_digits=20,
        decimal_places=5, 
        default=0.00  
    )
    
    # Standards
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)


class Compte(models.Model):
    
    class Meta:
        verbose_name = "Compte"
        verbose_name_plural = "Comptes"
        
        
    nom = models.CharField(max_length=256)
    operateur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="operateur_compte")
    type = models.CharField(max_length=256)
    numero_compte = models.CharField(
        max_length=20, 
        unique=True,    
    )

    
    # Standards
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)



class Paiement(models.Model):
    
    class Meta:
        verbose_name = "Paiement"
        verbose_name_plural = "Paiements"
        
    
    montant = models.DecimalField(
        max_digits=20,
        decimal_places=5, 
        default=0.00  
    )
    type = models.CharField(max_length=256)
    
    comptable = models.ForeignKey(Comptable, on_delete=models.PROTECT, related_name="comptable_Paiement")
    compte = models.ForeignKey(Compte, on_delete=models.PROTECT, related_name="compte_Paiement")

    facture = models.ForeignKey(Facture, on_delete=models.SET_NULL, null=True, related_name="facture_Paiement")
    nature = models.ForeignKey(Nature, on_delete=models.SET_NULL, null=True, related_name="nature_Paiement")
    rapportFinancier = models.ForeignKey(RapportFinancier, on_delete=models.SET_NULL, null=True, related_name="rapportFinancier_Paiement")
    
    # Standards
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    
