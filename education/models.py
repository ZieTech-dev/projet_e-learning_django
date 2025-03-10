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

    
    def __str__(self):
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

    def __str__(self):
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



    def __str__(self):
        return f"Évaluation - {self.jourComposition}"  # Affichage du jour de la composition uniquement
 
    def corriger(self):
        pass
        
   
    def donnerFeedback(self):
        pass