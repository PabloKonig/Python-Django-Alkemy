from django.urls import path
from .views import primera_vista, vista_html

app_name = 'autores_prueba'

urlpatterns = [
    path("primera/", primera_vista, name='primera_vista'),
    path("html/<str:dinamico>/<int:numero>/", vista_html, name='vista_html'),
]