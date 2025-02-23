from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def livraison(request):
  return render(request, 'livraison/livraison.html')