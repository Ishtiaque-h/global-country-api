from rest_framework import serializers
from .models import CountryData

class UserSerializer(serializers.ModelSerializer):
    code = serializers.CharField(source='cca2_name')
    
    class Meta:
        model = CountryData
        exclude = ['cca2_name', 'full_response', 'updated_by', 'updated_at']
