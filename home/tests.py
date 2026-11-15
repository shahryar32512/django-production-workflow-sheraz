from django.test import TestCase


class HomePageTests(TestCase):

    def test_homepage_returns_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_content(self):
        response = self.client.get('/')
        self.assertContains(
            response,
            'Home App - VS Code Integration Working!'
        )
