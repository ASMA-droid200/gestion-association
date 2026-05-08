from django.db import models

# Create your models here.
from django.db import models

class Document(models.Model):
    TYPES = [
        ('pv', 'Procès-verbal'),
        ('pdf', 'Document PDF'),
    ]

    titre = models.CharField(max_length=255)
    type_doc = models.CharField(max_length=10, choices=TYPES)
    fichier = models.FileField(upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre