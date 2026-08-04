from django.test import TestCase
from django.urls import reverse


class VallenatoViewTests(TestCase):
    def test_index_renders_collection_data(self):
        response = self.client.get(reverse("index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Coleccion del Lab2 en Django")
        self.assertContains(response, "Diomedes Diaz")
        self.assertContains(response, "Reproducciones")
        self.assertContains(response, "Destacado")

    def test_detail_route_renders_artist_nested_data(self):
        response = self.client.get(
            reverse("detalle_artista", kwargs={"slug": "diomedes-diaz"})
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "El Cacique de La Junta")
        self.assertContains(response, "Canciones Representativas")
        self.assertContains(response, "Sin medir distancias")

    def test_unknown_artist_returns_404(self):
        response = self.client.get(
            reverse("detalle_artista", kwargs={"slug": "artista-inexistente"})
        )

        self.assertEqual(response.status_code, 404)
