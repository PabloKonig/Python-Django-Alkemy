from django.shortcuts import render, get_object_or_404, redirect
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

def autor_cambiar_estado(request, id):
    autor = get_object_or_404(Autor, id=id)
    autor.activo = not(autor.activo)
    autor.save()
    return redirect("autores:autores_list")
        
class AutorCreateView(CreateView):
        model = Autor
        fields = ['nombre', 'fecha_nacimiento', 'fecha_fallecimiento', 'foto']
        template_name = 'autores/autores_edit.html'
        success_url = reverse_lazy('autores:autores_list')

class AutorUpdateView(UpdateView):
        model = Autor
        fields = ['nombre', 'fecha_nacimiento', 'fecha_fallecimiento', 'activo', 'foto']
        template_name = 'autores/autores_edit.html'
        success_url = reverse_lazy('autores:autores_list')

def autores_buscar(request):
       if request.method == 'POST':
                busqueda_autores = request.POST.get('buscar')
                resultado = Autor.objects.filter(nombre__contains=busqueda_autores)
                return render(request, 'autores/autores_list.html', {'autores': resultado})