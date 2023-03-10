from django.urls import path
from .views import RegisterView, VerifyEmail, LoginAPIView, getUser
from rest_framework_simplejwt.views import (TokenRefreshView)

urlpatterns = [
    path('user/<str:pk>', getUser, name='user'),
    path('register/', RegisterView.as_view(), name="register"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] 