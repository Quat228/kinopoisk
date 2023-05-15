from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from . import models
from . import serializers
from . import permissions


class UserRegisterAPIView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserRegisterSerializer


class ProfileRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = [permissions.ReadOnlyOrIsAuthor]


