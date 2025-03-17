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




# models.py - Modèles mis à jour
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, related_name='students')
    
    def __str__(self):
        return self.user.username

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='notes')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='notes')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Evaluation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='evaluations')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='evaluations')
    score = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.student.user.username} - {self.course.name} - {self.score}"

# Nouveaux modèles pour les fonctionnalités demandées
class Quiz(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='quizzes')
    description = models.TextField()
    time_limit = models.IntegerField(help_text="Temps limite en minutes", default=30)
    
    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    
    def __str__(self):
        return self.text[:50]
    
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text

class QuizAttempt(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='quiz_attempts')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='attempts')
    score = models.FloatField(null=True, blank=True)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.student.user.username} - {self.quiz.title}"
    
    def is_completed(self):
        return self.completed_at is not None


    

class StudentAnswer(models.Model):
    attempt = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE, related_name='student_answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def is_correct(self):
        return self.selected_choice.is_correct

    is_correct.boolean = True  # Pour afficher une icône dans l'interface d'administration
    is_correct.short_description = 'Correct ?'  # Libellé personnalisé

    def __str__(self):
        return f"{self.attempt.student.user.username} - {self.question.text[:50]}"


class Discussion(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='discussions')
    created_by = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='created_discussions')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Message(models.Model):
    content = models.TextField()
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='messages')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.author.user.username} - {self.created_at}"

class Invoice(models.Model):
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('paid', 'Payée'),
        ('cancelled', 'Annulée'),
    ]
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='invoices')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    payment_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Facture {self.id} - {self.student.user.username} - {self.amount} FCFA"
    
    def is_overdue(self):
        from datetime import date
        if self.due_date is None:  # Handle the case where due_date is None
            return False  # or return a custom message like "No due date set"
        return self.due_date < date.today()

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('card', 'Carte bancaire'),
        ('transfer', 'Virement bancaire'),
        ('cheque', 'Chèque'),
    ]
    
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Paiement {self.id} - {self.invoice.student.user.username} - {self.amount} FCFA"