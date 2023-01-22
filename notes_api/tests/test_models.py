from notes_api.models import Note
from authentication.models import User
from django.test import TestCase

class TestModel(TestCase):

    def tests_should_create_note(self):
        user=User.objects.create(username='username', email='email@app.com')
        user.set_password('password12!')
        user.save()
        note = Note(title="Note", body="Here is the description", owner=user)
        self.assertEqual(str(note), 'Note')