from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .tasks import send_welcome_email

class PublicAPI(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"message": "This is a public API endpoint."})

class ProtectedAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hello, {request.user.username}! This is a protected API."})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/api/protected/')
        else:
            return render(request, 'login.html', {'error': 'Invalid login'})
    return render(request, 'login.html')

class UserRegistrationAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password or not email:
            return Response({'error': 'Missing fields'}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=400)

        user = User.objects.create_user(username=username, password=password, email=email)

        # Call Celery Task
        send_welcome_email.delay(email)

        return Response({'message': 'User registered successfully. Welcome email sent.'})