from django.db import models

class Question(models.Model):
    reponse = models.TextField(verbose_name="Réponse")
    points = models.IntegerField(verbose_name="Points")

    def __str__(self):
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

    def __str__(self):
        return f"Note {self.id}"

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"
        
         # Champs standards
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de mise à jour")