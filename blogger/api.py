from . import models
from . import serializers
from rest_framework import viewsets, permissions


class BloggerProfileViewSet(viewsets.ModelViewSet):
    """ViewSet for the BloggerProfile class"""

    queryset = models.BloggerProfile.objects.all()
    serializer_class = serializers.BloggerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


