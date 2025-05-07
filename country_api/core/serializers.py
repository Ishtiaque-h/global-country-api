from rest_framework import serializers
from .models import CountryData

class CountrySerializer(serializers.ModelSerializer):
    cca2 = serializers.CharField(source='cca2_name')
    
    class Meta:
        model = CountryData
        exclude = ['cca2_name']
        
    def __init__(self, *args, **kwargs):
        exclude_fields = kwargs.pop('exclude_fields', False)
        super().__init__(*args, **kwargs)

        if exclude_fields:
            for field in ['full_response', 'updated_by', 'updated_at']:
                self.fields.pop(field, None)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()