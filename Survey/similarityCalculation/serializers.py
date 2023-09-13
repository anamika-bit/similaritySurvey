from rest_framework import serializers
from .models import Survey,similarityScore

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'

class similarityScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = similarityScore
        fields = '__all__'