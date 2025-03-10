from django.db import models

# Create your models here.

class Filiere(models.Model):  
    nom = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    # Standards
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Filere"
        verbose_name_plural = "Filieres"
        ordering = ['-created_at']  
    
    def __str__(self):
        return self.nom
    

class Niveau(models.Model):
    nom = models.CharField(max_length=255)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, related_name='niveaux')
    
    # Standards
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Niveau"
        verbose_name_plural = "Niveaux"
        ordering = ['-created_at'] 
    
    def __str__(self):
        return f"{self.nom} - {self.filiere}"
    

class Matiere(models.Model):
    nom = models.CharField(max_length=255)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE, related_name='matieres')
    # Standards
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Matiere"
        verbose_name_plural = "Matieres"
        ordering = ['-created_at'] 
    
    def __str__(self):
        return self.nom


class Module(models.Model):
    nom = models.CharField(max_length=255)
    coef = models.IntegerField()
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name='modules')
    
    # Standards
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Module"
        verbose_name_plural = "Modules"
        ordering = ['-created_at']  
    
    def __str__(self):
        return f"{self.nom} (Coef: {self.coef})"
    

class Cours(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    contenu = models.TextField()
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='cours')
    # Standards
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def ajouter_forum(self):
        # Logique pour ajouter un forum au cours
        pass
    
    def publier_contenu(self):
        # Logique pour publier le contenu du cours
        pass
    
    def __str__(self):
        return self.titre

class Lecon(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    contenu = models.TextField()
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, related_name='lecons')
    
    # Standards
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Leçon"
        verbose_name_plural = "Leçons"
        ordering = ['-created_at']  
    def ajouter_forum(self):
        # Logique pour ajouter un forum à la leçon
        pass
    
    def publier_contenu(self):
        # Logique pour publier le contenu de la leçon
        pass
    
    def __str__(self):
        return self.titre

class Chapitre(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    contenu = models.TextField()
    lecon = models.ForeignKey(Lecon, on_delete=models.CASCADE, related_name='chapitres')
    # Standards
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Chapitre"
        verbose_name_plural = "Chapitres"
        ordering = ['-created_at'] 
    
    
    def ajouter_forum(self):
        # Logique pour ajouter un forum au chapitre
        pass
    
    def publier_contenu(self):
        # Logique pour publier le contenu du chapitre
        pass
    
    def __str__(self):
        return self.titre

