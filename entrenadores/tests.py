from unittest.mock import Mock, patch

import requests
from django.test import TestCase


class ListaEntrenadoresTests(TestCase):
    @patch("requests.get")
    def test_muestra_entrenadores_recibidos_desde_la_api(self, mocked_get):
        """Un cambio que no entregue el JSON al template debe fallar aquí."""
        mocked_response = Mock()
        mocked_response.json.return_value = [
            {
                "entrenador_id": 1,
                "nombre": "Ana",
                "especialidad": "Fuerza",
                "anios_experiencia": 8,
            }
        ]
        mocked_get.return_value = mocked_response

        response = self.client.get("/entrenadores/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ana")
        self.assertContains(response, "Fuerza")
        self.assertContains(response, "8")

    @patch("requests.get", side_effect=requests.RequestException)
    def test_muestra_un_mensaje_cuando_la_api_no_responde(self, mocked_get):
        """Un cambio que omita el manejo de errores de red debe fallar aquí."""
        response = self.client.get("/entrenadores/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No fue posible obtener los entrenadores")
