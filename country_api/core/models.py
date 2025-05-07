from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class CountryData(models.Model):
    common_name = models.CharField(max_length=255, blank=False, null=False, default="")
    official_name = models.TextField(blank=False, null=False, default="")
    cca2_name = models.CharField(max_length=10, blank=False, null=False, default="", unique=True)
    region = models.CharField(max_length=100, blank=False, null=False, default="")
    subregion = models.CharField(max_length=150, blank=False, null=False, default="")
    capital = models.CharField(max_length=255, blank=False, null=False, default="")
    languages = ArrayField(models.CharField(max_length=50), blank=True, default=list)
    latitude = models.FloatField()
    longitude = models.FloatField()
    area = models.FloatField()
    population = models.IntegerField()
    flag = models.TextField(blank=False, null=False, default="")
    timezones = ArrayField(models.CharField(max_length=20), blank=True, default=list)
    full_response = models.JSONField(default=dict)
    updated_by = models.ForeignKey(User, blank=True, null=True, related_name="countries", on_delete=models.SET_NULL)
    updated_at = models.DateTimeField(null=False)
    
    @property
    def get_timezones(self):
        return ", ".join(self.timezones)

