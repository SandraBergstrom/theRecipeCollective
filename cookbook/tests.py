from django.test import TestCase
import unittest


class URLTests(TestCase):
    def test_landingpage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
