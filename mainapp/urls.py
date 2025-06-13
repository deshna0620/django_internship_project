from django.urls import path
from .views import PublicAPI, ProtectedAPI, user_login, UserRegistrationAPI

urlpatterns = [
    path('items/', PublicAPI.as_view(), name='public_api'),
    path('protected/', ProtectedAPI.as_view(), name='protected_api'),
    path('register/', UserRegistrationAPI.as_view(), name='register_api'),
    path('login/', user_login, name='login'),
]