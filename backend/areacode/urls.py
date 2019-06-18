from django.urls import path, include
from rest_framework.routers import DefaultRouter

from areacode.views import ProvinceViewSet,\
    RegencyViewSet, DistrictViewSet, VillageViewSet

router = DefaultRouter()
router.register('province', ProvinceViewSet)
router.register(r'regency', RegencyViewSet, base_name='regency')
router.register(r'district', DistrictViewSet, base_name='district')
router.register(r'village', VillageViewSet, base_name='village')

app_name = 'areacode'

urlpatterns = [

    path('', include(router.urls)),
]
