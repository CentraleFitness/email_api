from emailapp.models import Proximity, NewsletterRecipient
from rest_framework import serializers

class ProximitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Proximity
        fields = ('email', 'city')

class NewsletterRecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterRecipient
        fields = ('email', )

class NewsletterRecipientOptOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterRecipient
        fields = ('email', 'opt_out')
