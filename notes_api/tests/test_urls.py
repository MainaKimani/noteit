from django.test import SimpleTestCase
from django.urls import reverse, resolve
from notes_api.views import getNotes, createNote, updateNote, deleteNote, getNote

class authURLtests(SimpleTestCase):

    def test_get_notes_list_is_resolved(self):
        url = reverse('notes')
        self.assertEquals(resolve(url).func, getNotes)
    
    def test_create_note_is_resolved(self):
        url = reverse('create-note')
        self.assertEquals(resolve(url).func, createNote)
    
    def test_update_note_is_resolved(self):
        url = reverse('update-note', args=[1])
        self.assertEquals(resolve(url).func, updateNote)
    
    def test_delete_note_is_resolved(self):
        url = reverse('delete-note', args=[1])
        self.assertEquals(resolve(url).func, deleteNote)

    def test_get_note_is_resolved(self):
        url = reverse('note', args=[1])
        self.assertEquals(resolve(url).func, getNote)
    

    
    