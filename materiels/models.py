from django.db import models

class Materiel(models.Model):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    quantite = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.nom

