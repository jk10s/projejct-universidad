from django.urls import path
from .models import *
from .views import *

urlpatterns = [
    path('', lista.as_view(), name='Gestion de cursos'),
    path('eliminacion/<int:id>', eliminacion),
    path('registrarcurso/', registrarcurso),
    path('edicion/<int:id>', editar),
    path('editarcurso/', editarcurso),
]
