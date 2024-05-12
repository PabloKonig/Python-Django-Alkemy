from django.urls import path
from .views import FrasesListView, FrasesCreateView, FrasesUpdateView

app_name = 'frases'

urlpatterns = [
    path('', FrasesListView.as_view(), name='frases_list'),
    path('crear/', FrasesCreateView.as_view(), name='frases_crear'),
    path('edit/<int:pk>/', FrasesUpdateView.as_view(), name='frases_modificar'),
]
