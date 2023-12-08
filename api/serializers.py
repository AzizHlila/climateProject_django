from rest_framework import serializers
from api.models import Factors,Information

class FactorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factors
        fields = ('name', 'description')

class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ('title', 'description',"is_true")