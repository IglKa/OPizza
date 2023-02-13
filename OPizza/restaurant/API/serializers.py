from rest_framework import serializers

from ..models import Restaurant


class RestautantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('name', 'rating')
