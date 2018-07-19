from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

from rest_framework import generics, mixins

from emailapp.models import Proximity, NewsletterRecipient
from emailapp.serializers import ProximitySerializer
from emailapp.serializers import NewsletterRecipientSerializer

class ProximityAlertAPI(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    queryset = Proximity.objects.all()
    serializer_class = ProximitySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class NewsletterRecipientAPI(mixins.CreateModelMixin,
                             generics.GenericAPIView):
    queryset = NewsletterRecipient.objects.all()
    serializer_class = NewsletterRecipientSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class NewsletterRecipientListAPI(mixins.ListModelMixin,
                                 generics.GenericAPIView):
    queryset = NewsletterRecipient.objects.all()
    serializer_class = NewsletterRecipientSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class NewsletterUnsubscribeAPI(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = NewsletterRecipient.objects.all()
    serializer_class = NewsletterRecipientSerializer

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
