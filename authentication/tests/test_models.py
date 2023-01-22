from authentication.models import User
from django.test import TestCase

class TestModel(TestCase):
    def tests_should_create_user(self):
        user=User.objects.create(username='username', email='email@app.com')
        user.set_password('password12!')
        user.save()

        self.assertEqual(str(user), 'email@app.com')