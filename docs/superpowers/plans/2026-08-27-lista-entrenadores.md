# Lista de entrenadores Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Crear una página Django en `/entrenadores/` que consulte FastAPI y muestre entrenadores en una tabla.

**Architecture:** El proyecto `config` publica las URLs raíz. La aplicación `entrenadores` encapsula la consulta HTTP y el renderizado de la plantilla; captura errores de `requests` y entrega al template una lista vacía junto con un mensaje.

**Tech Stack:** Python, Django, requests, HTML y CSS.

**Spec:** `docs/superpowers/specs/2026-08-27-lista-entrenadores-design.md`

## Global Constraints

- La API objetivo es `http://127.0.0.1:8000/entrenadores`.
- FastAPI permanece en el puerto 8000; Django se ejecuta en el 8001.
- La ruta pública debe ser `/entrenadores/`.
- La tabla muestra ID, Nombre, Especialidad y Años de experiencia.

---

### Task 1: Inicializar el proyecto Django

**Files:**
- Create: `requirements.txt`
- Create: `manage.py`
- Create: `config/__init__.py`
- Create: `config/settings.py`
- Create: `config/urls.py`
- Create: `config/asgi.py`
- Create: `config/wsgi.py`

**Interfaces:**
- Produces: proyecto Django ejecutable con `python manage.py test`.

- [ ] **Step 1: Declarar dependencias**

```text
Django
requests
```

- [ ] **Step 2: Instalar dependencias en el entorno de trabajo**

Run: `python -m pip install -r requirements.txt`

- [ ] **Step 3: Generar el proyecto con el paquete config**

Run: `python -m django startproject config .`

- [ ] **Step 4: Verificar la configuración base**

Run: `python manage.py check`
Expected: `System check identified no issues`.

### Task 2: Probar e implementar la vista de entrenadores

**Files:**
- Create: `entrenadores/tests.py`
- Create: `entrenadores/views.py`
- Create: `entrenadores/urls.py`
- Modify: `config/settings.py`
- Modify: `config/urls.py`

**Interfaces:**
- Consumes: `GET http://127.0.0.1:8000/entrenadores`.
- Produces: `lista_entrenadores(request)` y la ruta `/entrenadores/`.

- [ ] **Step 1: Escribir pruebas que fallen**

```python
@patch("entrenadores.views.requests.get")
def test_lista_muestra_entrenadores(self, mocked_get):
    mocked_get.return_value.json.return_value = [{
        "entrenador_id": 1,
        "nombre": "Ana",
        "especialidad": "Fuerza",
        "anios_experiencia": 8,
    }]
    mocked_get.return_value.raise_for_status.return_value = None
    response = self.client.get("/entrenadores/")
    self.assertContains(response, "Ana")

@patch("entrenadores.views.requests.get", side_effect=requests.RequestException)
def test_lista_muestra_mensaje_si_api_no_responde(self, mocked_get):
    response = self.client.get("/entrenadores/")
    self.assertContains(response, "No fue posible obtener los entrenadores")
```

- [ ] **Step 2: Ejecutar las pruebas para verificar el fallo**

Run: `python manage.py test entrenadores`
Expected: FAIL porque la aplicación y la vista aún no existen.

- [ ] **Step 3: Implementar la aplicación y las URLs**

```python
def lista_entrenadores(request):
    error = None
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        entrenadores = response.json()
    except (requests.RequestException, ValueError):
        entrenadores = []
        error = "No fue posible obtener los entrenadores. Inténtalo de nuevo más tarde."
    return render(request, "entrenadores/lista.html", {"entrenadores": entrenadores, "error": error})
```

- [ ] **Step 4: Ejecutar las pruebas para verificar el éxito**

Run: `python manage.py test entrenadores`
Expected: PASS.

### Task 3: Crear la interfaz y comprobar el proyecto

**Files:**
- Create: `entrenadores/templates/entrenadores/lista.html`
- Create: `entrenadores/static/entrenadores/css/lista.css`

**Interfaces:**
- Consumes: `entrenadores` y `error` del contexto de `lista_entrenadores`.
- Produces: tabla HTML con las cuatro columnas solicitadas.

- [ ] **Step 1: Crear plantilla con el bucle de entrenadores**

```html
{% for entrenador in entrenadores %}
<tr>
  <td>{{ entrenador.entrenador_id }}</td>
  <td>{{ entrenador.nombre }}</td>
  <td>{{ entrenador.especialidad }}</td>
  <td>{{ entrenador.anios_experiencia }}</td>
</tr>
{% empty %}
<tr><td colspan="4">No hay entrenadores disponibles.</td></tr>
{% endfor %}
```

- [ ] **Step 2: Añadir estilos locales para la tabla**

```css
table { width: 100%; border-collapse: collapse; }
th, td { padding: 0.75rem; border-bottom: 1px solid #dfe3e8; }
```

- [ ] **Step 3: Ejecutar todas las pruebas y las comprobaciones de Django**

Run: `python manage.py test && python manage.py check`
Expected: todas las pruebas PASS y ninguna incidencia de configuración.
