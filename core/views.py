from django.http import HttpResponse
from django.views import View
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics, status
from rest_framework.views import APIView

# We need these for the views below
from .models import User, Profile 
from .serializers import UserRegistrationSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    """A simple view to see if the API is running."""
    return Response({"status": "healthy"}, status=status.HTTP_200_OK)

class AboutView(View):
    """A standard Django class-based view."""
    def get(self, request):
        return HttpResponse("Team Task Tracker API", status=200, content_type="text/plain")

@api_view(['GET'])
@permission_classes([AllowAny])
def forbidden_view(request):
    """The missing view that was causing the error."""
    return Response({"detail": "This is a custom forbidden message"}, status=status.HTTP_403_FORBIDDEN)

class RegisterView(generics.CreateAPIView):
    """View to register new users."""
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

class UserProfileView(APIView):
    """View to see logged-in user details."""
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({
            "username": request.user.username,
            "email": request.user.email,
            "role": request.user.role
        })