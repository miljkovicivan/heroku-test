from rest_framework import serializers
from .models import Dog, Cat

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Dog

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Cat
