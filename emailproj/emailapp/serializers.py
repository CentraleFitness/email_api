from emailapp.models import Proximity
from rest_framework import serializers

class ProximitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proximity
        fields = ('email', 'city')
