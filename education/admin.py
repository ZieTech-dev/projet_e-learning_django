from django.contrib import admin
from .models import Classe, TypeEvaluation, Evaluation, Question, Note, Filiere, Niveau, Matiere, Module, Cours, Lecon, Chapitre

# Classe d'administration pour le modèle Classe
class ClasseAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'nombreEtudiant', 'statut', 'created_at', 'updated_at')
    search_fields = ('nom', 'description')
    list_filter = ('statut',)

# Classe d'administration pour le modèle TypeEvaluation
class TypeEvaluationAdmin(admin.ModelAdmin):
    list_display = ('nom', 'total', 'statut', 'created_at', 'updated_at')
    search_fields = ('nom',)
    list_filter = ('statut',)

# Classe d'administration pour le modèle Evaluation
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('jourComposition', 'tentatives', 'durée', 'datecreation', 'heurecomposition', 'datelimite')
    search_fields = ('jourComposition', 'datecreation')
    list_filter = ('jourComposition',)

# Classe d'administration pour le modèle Question
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'points', 'created_at', 'updated_at')
    search_fields = ('id',)
    list_filter = ('created_at',)

# Classe d'administration pour le modèle Note
class NoteAdmin(admin.ModelAdmin):
    list_display = ('noteobtenu', 'nombrereponsecorrect', 'nombrereponseIncorrect', 'created_at', 'updated_at')
    search_fields = ('noteobtenu',)
    list_filter = ('created_at',)

# Classe d'administration pour le modèle Filiere
class FiliereAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'statut', 'created_at', 'last_updated_at')
    search_fields = ('nom', 'description')
    list_filter = ('statut',)

# Classe d'administration pour le modèle Niveau
class NiveauAdmin(admin.ModelAdmin):
    list_display = ('nom', 'filiere', 'statut', 'created_at', 'last_updated_at')
    search_fields = ('nom',)
    list_filter = ('filiere', 'statut')

# Classe d'administration pour le modèle Matiere
class MatiereAdmin(admin.ModelAdmin):
    list_display = ('nom', 'niveau', 'statut', 'created_at', 'last_updated_at')
    search_fields = ('nom',)
    list_filter = ('niveau', 'statut')

# Classe d'administration pour le modèle Module
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('nom', 'coef', 'matiere', 'statut', 'created_at', 'last_updated_at')
    search_fields = ('nom',)
    list_filter = ('matiere', 'statut')

# Classe d'administration pour le modèle Cours
class CoursAdmin(admin.ModelAdmin):
    list_display = ('titre', 'module', 'statut', 'created_at', 'last_updated_at')
    search_fields = ('titre',)
    list_filter = ('module', 'statut')

# Classe d'administration pour le modèle Lecon
class LeconAdmin(admin.ModelAdmin):
    list_display = ('titre', 'cours', 'statut', 'created_at', 'last_updated_at')
    search_fields = ('titre',)
    list_filter = ('cours', 'statut')

# Classe d'administration pour le modèle Chapitre
class ChapitreAdmin(admin.ModelAdmin):
    list_display = ('titre', 'lecon', 'statut', 'created_at', 'last_updated_at')
    search_fields = ('titre',)
    list_filter = ('lecon', 'statut')

# Enregistrement des modèles et de leurs classes d'administration respectives
admin.site.register(Classe, ClasseAdmin)
admin.site.register(TypeEvaluation, TypeEvaluationAdmin)
admin.site.register(Evaluation, EvaluationAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Filiere, FiliereAdmin)
admin.site.register(Niveau, NiveauAdmin)
admin.site.register(Matiere, MatiereAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Cours, CoursAdmin)
admin.site.register(Lecon, LeconAdmin)
admin.site.register(Chapitre, ChapitreAdmin)
