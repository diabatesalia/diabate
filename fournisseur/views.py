from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def list_fournisseur(request):
  return HttpResponse('La page des fournisseurs')