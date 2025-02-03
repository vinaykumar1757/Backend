from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import FAQ

class FAQTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.faq = FAQ.objects.create(
            question_en="Test question",
            answer_en="<p>Test answer</p>"
        )

    def test_translation_creation(self):
        self.assertNotEqual(self.faq.question_hi, '')
        self.assertNotEqual(self.faq.answer_hi, '')

    def test_api_response(self):
        response = self.client.get('/api/faqs/?lang=hi')
        self.assertEqual(response.status_code, 200)
        self.assertIn('परीक्षण', response.data[0]['question'])
