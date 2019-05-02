""" module to test views to api """

from django.test import TestCase

class TestView(TestCase):
    """ Teste Views """

    def test_index(self):
        
        resp = self.client.get("/loans/")
        self.assertEqual(resp.status_code, 200)

        self.assertEqual(resp.text, "We are under construction = )")        
        