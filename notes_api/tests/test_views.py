from notes_api.models import Note
from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('notes')
        self.detail_url = reverse('note', args=[1])
    
    def test_cannot_GET_notes_list_without_authToken(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 401)
    
    def test_cannot_GET_notes_detail_without_authToken(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 401)
    
    
    
    
        