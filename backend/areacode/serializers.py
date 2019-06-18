from rest_framework import serializers

from areacode.models import Province, Regency, District, Village


class ProvinceSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="areacode:province-detail")

    class Meta:
        model = Province()
        fields = ('id', 'url', 'name')


class RegencySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="areacode:regency-detail")

    class Meta:
        model = Regency()
        fields = ('id', 'url', 'name', 'province_id',)


class DistrictSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="areacode:district-detail")

    class Meta:
        model = District()
        fields = ('id', 'url', 'name', 'regency_id',)


class VillageSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="areacode:village-detail")

    class Meta:
        model = Village()
        fields = ('id', 'url', 'name', 'district_id',)
