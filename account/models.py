from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    PHOTO_PROFILE_UPLOAD_PATH = "profile_photos"
    ROLE_CHOICES = [
        ('ETUDIANT', 'Etudiant'),
        ('ENSEIGNANT', 'Enseignant'),
        ('RESPONSABLE_SCOLARITE', 'Responsable scolarité'),
        ('ADMINISTRATEUR', 'Administrateur'),
        ('COMPTABLE', 'Comptable'),
        ('null', 'null'),
    ]

    photo_profile = models.ImageField(upload_to=PHOTO_PROFILE_UPLOAD_PATH, default="profile/icon_profile.png")
    numero_telephone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True)
    rue = models.CharField(blank=True, max_length=255)
    ville = models.CharField(blank=True, max_length=100)
    code_postal = models.CharField(blank=True, max_length=20)
    pays = models.CharField(blank=True, max_length=100)
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='null')

    def save(self, *args, **kwargs):
        if self.rue or self.ville or self.pays:
            self.address = f"{self.rue}, {self.ville}, {self.pays}".strip(', ')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

    def is_etudiant(self):
        return self.role == 'ETUDIANT'

    def is_enseignant(self):
        return self.role == 'ENSEIGNANT'

    def is_responsable_scolarite(self):
        return self.role == 'RESPONSABLE_SCOLARITE'

    def is_administrateur(self):
        return self.role == 'ADMINISTRATEUR'

    def is_comptable(self):
        return self.role == 'COMPTABLE'


class Etudiant(CustomUser):
    matricule = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return f"Etudiant: {self.username}"


class Enseignant(CustomUser):
    matricule = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return f"Enseignant: {self.username}"

