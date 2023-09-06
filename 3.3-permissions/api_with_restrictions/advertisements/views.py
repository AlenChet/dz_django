from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

from .filters import AdvertisementFilter
from .models import Advertisement
from .permissions import IsAuthorOrReadOnly
from .serializers import AdvertisementSerializer


class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
        else:
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()