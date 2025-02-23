from django.db import models

# Create your models here.
class Stock(models.Model):
  #nom_fournisseur = 
  #telephone_fournisseu =
  quantite = models.CharField(max_length=200,null=True)
  somme = models.CharField(max_length=100,null=True)
  date = models.DateField(auto_now_add=True)