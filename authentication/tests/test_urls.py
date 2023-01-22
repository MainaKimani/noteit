from django.test import SimpleTestCase
from django.urls import reverse, resolve
from authentication.views import LoginAPIView, RegisterView, VerifyEmail, getUser

class authURLtests(SimpleTestCase):

    def test_login_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, LoginAPIView) 
    
    def test_register_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func.view_class, RegisterView)
    
    def test_verifyEmail_is_resolved(self):
        url = reverse('email-verify')
        self.assertEquals(resolve(url).func.view_class, VerifyEmail)

    def test_get_user_is_resolved(self):
        url = reverse('user', args=[1])
        self.assertEquals(resolve(url).func, getUser)
    
    