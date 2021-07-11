from rest_framework import generics, serializers

from user.serializers import UserSerializer

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer
    