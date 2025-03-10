from django.contrib import admin
from .models import CustomUser, Etudiant, Enseignant, Comptable, Administrateur, ResponsableScolarite
from django.contrib.auth.admin import UserAdmin

# Personnalisation du modèle CustomUser dans l'admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'first_name', 'last_name', 'email', 'role', 'is_active', 'is_staff', 'date_joined')
    list_filter = ('role', 'is_active', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-date_joined',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'photo_profile', 'bio', 'address')}),
        ('Additional Info', {'fields': ('numero_telephone', 'rue', 'ville', 'code_postal', 'pays', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'role'),
        }),
    )

# Personnalisation du modèle Etudiant dans l'admin
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('username', 'matricule', 'role', 'is_active', 'date_joined')
    list_filter = ('role', 'is_active')
    search_fields = ('username', 'matricule')
    ordering = ('-date_joined',)

# Personnalisation du modèle Enseignant dans l'admin
class EnseignantAdmin(admin.ModelAdmin):
    list_display = ('username', 'matricule', 'role', 'is_active', 'date_joined')
    list_filter = ('role', 'is_active')
    search_fields = ('username', 'matricule')
    ordering = ('-date_joined',)

# Personnalisation du modèle Comptable dans l'admin
class ComptableAdmin(admin.ModelAdmin):
    list_display = ('username', 'matricule', 'role', 'is_active', 'date_joined')
    list_filter = ('role', 'is_active')
    search_fields = ('username', 'matricule')
    ordering = ('-date_joined',)

# Personnalisation du modèle Administrateur dans l'admin
class AdministrateurAdmin(admin.ModelAdmin):
    list_display = ('username', 'matricule', 'role', 'is_active', 'date_joined')
    list_filter = ('role', 'is_active')
    search_fields = ('username', 'matricule')
    ordering = ('-date_joined',)

# Personnalisation du modèle ResponsableScolarite dans l'admin
class ResponsableScolariteAdmin(admin.ModelAdmin):
    list_display = ('username', 'matricule', 'role', 'is_active', 'date_joined')
    list_filter = ('role', 'is_active')
    search_fields = ('username', 'matricule')
    ordering = ('-date_joined',)

# Enregistrer les modèles avec leurs personnalisations
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Etudiant, EtudiantAdmin)
admin.site.register(Enseignant, EnseignantAdmin)
admin.site.register(Comptable, ComptableAdmin)
admin.site.register(Administrateur, AdministrateurAdmin)
admin.site.register(ResponsableScolarite, ResponsableScolariteAdmin)
