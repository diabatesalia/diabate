from django.db import models

# Create your models here.

class Livraison(models.Model):
  #nom = 
  #telephone =
  #ville =
  quantite = models.CharField(max_length=200,null=True)
  somme = models.CharField(max_length=200,null=True)
  date_livraison = models.DateField(auto_now_add=True,null=True)