from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "project": "Django Internship Project",
        "status": "Running",
        "message": "Welcome to the API backend.",
        "available_endpoints": [
            "/api/items/ - Public endpoint",
            "/api/protected/ - JWT Protected endpoint",
            "/api/register/ - User Registration",
            "/api/token/ - Get JWT Token"
        ]
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('mainapp.urls')),
    path('', home),
]