# Lista de entrenadores

## Objetivo

Inicializar un proyecto Django mínimo que consulte la API FastAPI local y presente los entrenadores en una tabla HTML.

## Estructura

- `config` contendrá la configuración del proyecto y las URLs raíz.
- `entrenadores` será la aplicación que contiene la vista, las URLs, la plantilla, los estáticos y las pruebas.
- `requirements.txt` declarará Django y requests.

## Flujo de datos

Una petición a `/entrenadores/` invoca `lista_entrenadores`. La vista solicita `GET http://127.0.0.1:8000/entrenadores` con un tiempo de espera finito. Ante una respuesta HTTP satisfactoria, entrega el JSON al template como `entrenadores`. Ante un error de red, tiempo de espera, JSON inválido o respuesta HTTP de error, entrega una lista vacía y un mensaje legible.

## Interfaz

La plantilla iterará con `{% for %}` y mostrará las columnas ID, Nombre, Especialidad y Años de experiencia. Incluirá un CSS estático de la aplicación para una tabla sencilla y legible. Si la lista no contiene registros, mostrará una fila informativa.

## Pruebas

Las pruebas de Django sustituirán la llamada HTTP para comprobar el contexto y el contenido HTML de una respuesta correcta, así como el mensaje y la lista vacía al producirse un error de conexión.

## Ejecución

FastAPI continuará en el puerto 8000. Django se iniciará en el puerto 8001 y la página se comprobará en `http://127.0.0.1:8001/entrenadores/`.
