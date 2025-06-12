from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ItemListCreateView, ProtectedView

urlpatterns = [
    path('items/', ItemListCreateView.as_view(), name='item-list'),      # Public
    path('protected/', ProtectedView.as_view(), name='protected'),       # Protected
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login (Token Generation)
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Refresh Token
]