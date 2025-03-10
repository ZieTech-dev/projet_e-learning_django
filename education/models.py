from django.db import models

class Classe(models.Model):

    class Meta:
        verbose_name = "Classe"
        verbose_name_plural = "Classes"

    
    # champs standars
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    statut=models.BooleanField(default=False)


    nom = models.CharField(max_length=255, verbose_name="Nom de la classe")
    description = models.TextField(verbose_name="Description de la classe")
    image = models.ImageField(upload_to='images/cours/', verbose_name="Image de la classe")
    nombreEtudiant = models.IntegerField(verbose_name="Nombre d'étudiants")

    
    def _str_(self):
        return self.nom  

class TypeEvaluation(models.Model):
    class Meta:
        verbose_name = "Type d'évaluation"
        verbose_name_plural = "Types d'évaluation"

    # champs standars
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    statut=models.BooleanField(default=False)

    nom = models.CharField(max_length=255, verbose_name="Nom du type d'évaluation")
    total = models.IntegerField(verbose_name="Total des points")

    def _str_(self):
        return self.nom 

class Evaluation(models.Model):
    class Meta:
        verbose_name = "Évaluation"
        verbose_name_plural = "Évaluations"

    tentatives = models.IntegerField(verbose_name="Nombre de tentatives")
    durée = models.DurationField(verbose_name="Durée de l'évaluation")
    datecreation = models.DateField(verbose_name="Date de création")
    heurecomposition = models.DateTimeField(verbose_name="Heure de composition")
    datelimite = models.DateTimeField(verbose_name="Date limite")
    jourComposition = models.CharField(max_length=100, verbose_name="Jour de la composition")



    def _str_(self):
        return f"Évaluation - {self.jourComposition}"  # Affichage du jour de la composition uniquement
 
    def corriger(self):
        pass
        
   
    def donnerFeedback(self):
        pass

class Question(models.Model):
    reponse = models.TextField(verbose_name="Réponse")
    points = models.IntegerField(verbose_name="Points")

    def _str_(self):
        return f"Question {self.id}"

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        
        
         # Champs standards
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de mise à jour")
        
    
class Note(models.Model):
    nombrereponsecorrect = models.IntegerField(verbose_name="Nombre de réponses correctes")
    nombrereponseIncorrect = models.IntegerField(verbose_name="Nombre de réponses incorrectes")
    noteobtenu = models.FloatField(verbose_name="Note obtenue")
    appreciation = models.TextField(verbose_name="Appréciation")

    def _str_(self):
        return f"Note {self.id}"

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"
        
         # Champs standards
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de mise à jour")

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
    
    def _str_(self):
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
    
    def _str_(self):
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
    
    def _str_(self):
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
    
    def _str_(self):
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
    
    def _str_(self):
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
    
    def _str_(self):
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
    
    def _str_(self):
        return self.titre