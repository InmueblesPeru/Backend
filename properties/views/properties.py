# Django

from django.http import Http404

# Rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Model
from properties.models.properties import Property

# Serializers
from properties.serializers.properties import PropertyModelSerializer


class ListProperties(APIView):
    """View to list all properties in the system"""

    def get(self, request):
        """Return a list of all properties"""

        if request.data.get('id') != None:
            try:
                properties = Property.objects.get(pk=self.request.data.get('id'))
            except Property.DoesNotExist:
                raise Http404
            serializer = PropertyModelSerializer(properties)
        else:
            properties = Property.objects.all()
            serializer = PropertyModelSerializer(properties, many=True)

        return Response(serializer.data)
