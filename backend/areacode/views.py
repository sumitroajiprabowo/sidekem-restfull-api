from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from areacode.models import Province, Regency, District, Village
from areacode import serializers


class ProvinceViewSet(viewsets.ReadOnlyModelViewSet):
    """Manage tags in the database"""

    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Province.objects.all()
    serializer_class = serializers.ProvinceSerializer


class RegencyViewSet(viewsets.ReadOnlyModelViewSet):
    """Manage tags in the database"""
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = serializers.RegencySerializer

    def get_queryset(self):
        queryset = Regency.objects.all()
        province_id = self.request.query_params.get('province_id')

        if province_id is not None:
            queryset = queryset.filter(province_id=province_id)
        return queryset


class DistrictViewSet(viewsets.ReadOnlyModelViewSet):
    """Manage tags in the database"""
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = serializers.DistrictSerializer

    def get_queryset(self):
        queryset = District.objects.all()
        regency_id = self.request.query_params.get('regency_id')

        if regency_id is not None:
            queryset = queryset.filter(regency_id=regency_id)
        return queryset


class VillageViewSet(viewsets.ReadOnlyModelViewSet):
    """Manage tags in the database"""
    permission_classes = (AllowAny,)
    serializer_class = serializers.VillageSerializer

    def get_queryset(self):
        queryset = Village.objects.all()
        district_id = self.request.query_params.get('district_id')

        if district_id is not None:
            queryset = queryset.filter(district_id=district_id)
        return queryset
