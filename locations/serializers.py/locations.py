'''Profile serializers'''

# Rest framework
from rest_framework import serializers

# Model
from locations.models.countries import Countries, States, Cities, Neighborhoods

class CitiesModelSerializer(serializers.ModelSerializer):
    neighborhoods = serializers.StringRelatedField()

    class Meta:
        model = Cities
        fields = ['id', 'name', 'neighborhoods']
