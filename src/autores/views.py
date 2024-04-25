from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView
from .models import Autor
from django.urls import reverse_lazy

#Create your views here.
def autores_list(request):
        autores = Autor.objects.all()
        return render(request, 'autores/autores_list.html', {'autores': autores})

def autor_por_id(request, id):
        autor = get_object_or_404(Autor, id=id)
        return render(request, 'autores/autores_id.html', {'autor': autor})
        
class AutorCreateView(CreateView):
        model = Autor
        fields = ['nombre', 'fecha_nacimiento', 'fecha_fallecimiento', 'foto']
        template_name = 'autores/autores_edit.html'
        success_url = 'http://localhost:8000/autores/'

class AutorUpdateView(UpdateView):
        model = Autor
        fields = ['nombre', 'fecha_nacimiento', 'fecha_fallecimiento', 'activo', 'foto']
        template_name = 'autores/autores_edit.html'
        success_url = 'http://localhost:8000/autores/'