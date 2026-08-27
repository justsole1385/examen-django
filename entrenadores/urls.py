from django.urls import path

from . import views

urlpatterns = [
    path("", views.lista_entrenadores, name="lista_entrenadores"),
]
