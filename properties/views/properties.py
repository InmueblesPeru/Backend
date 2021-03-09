# Rest_framwork
from rest_framework.views import APIView
from rest_framework.response import Response

# Model
from properties.models.properties import Property

# Serializers
from properties.serializers.properties import PropertyModelSerializer


class ListProperties(APIView):
    '''View to list all properties in the system'''

    def get(self, request, format=None):
        '''Return a list of all properties'''
        properties = Property.objects.all()
        serializer = PropertyModelSerializer(properties, many=True)

        return Response(serializer.data)
