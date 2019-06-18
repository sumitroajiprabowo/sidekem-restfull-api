from django.db import models


class Province(models.Model):
    """Model Database Provinsi"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "provinces"


class Regency(models.Model):
    """Model Database Kabupaten"""
    name = models.CharField(max_length=255)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "regencies"


class District(models.Model):
    """Model Database Kecamatan"""
    name = models.CharField(max_length=255)
    regency = models.ForeignKey(Regency, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "districts"


class Village(models.Model):
    """Model Database Desa"""
    id = models.BigIntegerField(blank=False, primary_key=True)
    name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "villages"
