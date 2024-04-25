from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def primera_vista(request):
    return HttpResponse(content="Hola desde Django!!!!")

def vista_html(request, dinamico, numero):
    return render(request, 'prueba/prueba_template.html', { 'valor':dinamico, 'anios': numero })