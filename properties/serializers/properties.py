"""Profile serializers"""

# Rest framework
from rest_framework import serializers

# Model
from properties.models.properties import Property


class PropertyModelSerializer(serializers.ModelSerializer):
    """Property model serializer"""
    neighborhoods = serializers.StringRelatedField()

    class Meta:
        """Meta class"""

        model = Property
        fields = '__all__'
