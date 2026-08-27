import requests
from django.shortcuts import render


API_ENTRENADORES_URL = "http://127.0.0.1:8000/entrenadores"


def lista_entrenadores(request):
    """Consulta la API de entrenadores y presenta sus datos en una tabla."""
    entrenadores = []
    error = None

    try:
        response = requests.get(API_ENTRENADORES_URL, timeout=5)
        response.raise_for_status()
        entrenadores = response.json()
    except (requests.RequestException, ValueError):
        error = "No fue posible obtener los entrenadores. Inténtalo de nuevo más tarde."

    return render(
        request,
        "entrenadores/lista.html",
        {"entrenadores": entrenadores, "error": error},
    )
