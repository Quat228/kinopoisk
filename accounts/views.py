from rest_framework import generics
from rest_framework.generics import get_object_or_404
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


class ProfileCabinetApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Profile
    serializer_class = serializers.ProfileSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.request.user.profile.id)
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_destroy(self, instance):
        instance.user.delete()
