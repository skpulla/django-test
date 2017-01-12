from django.test import TestCase
from django.test import Client

class SimpleTest(TestCase):

    def test_simple(self):
        c = Client()

        response = c.get('/admin/', follow=True)

        self.assertEqual(200, response.status_code)
