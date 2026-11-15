from django.test import TestCase


class MenuPageTests(TestCase):

    def test_menu_page_returns_200(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)

    def test_menu_page_content(self):
        response = self.client.get('/menu/')
        self.assertContains(response, 'Welcome to Menu App!')
