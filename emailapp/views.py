from django.views import View
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

from rest_framework import generics, mixins

from emailapp.models import Proximity, NewsletterRecipient
from emailapp.serializers import ProximitySerializer
from emailapp.serializers import NewsletterRecipientSerializer
from emailapp.serializers import NewsletterRecipientOptOutSerializer
from emailapp.filters import RecipientOptFilterBackend
from emailapp.form import OptForm


class ProximityAlertAPI(mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    queryset = Proximity.objects.all()
    serializer_class = ProximitySerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ProximityAlertListAPI(mixins.ListModelMixin,
                            generics.GenericAPIView):
    queryset = Proximity.objects.all()
    serializer_class = ProximitySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class NewsletterRecipientAPI(mixins.CreateModelMixin,
                             generics.GenericAPIView):
    queryset = NewsletterRecipient.objects.all()
    serializer_class = NewsletterRecipientSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class NewsletterRecipientListAPI(mixins.ListModelMixin,
                                 generics.GenericAPIView):
    queryset = NewsletterRecipient.objects.all()
    filter_backends = [RecipientOptFilterBackend]
    serializer_class = NewsletterRecipientSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class NewsletterUnsubscribeAPI(mixins.UpdateModelMixin,
                               generics.GenericAPIView):
    queryset = NewsletterRecipient.objects.all()
    serializer_class = NewsletterRecipientOptOutSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data={}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class NewsletterManageAPI(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = NewsletterRecipient.objects.all()
    serializer_class = NewsletterRecipientOptOutSerializer

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ManageView(View):
    def get(self, request, pk):
        # magic happens here
        return render(request, 'emailapp/manage.html', {
            'form': OptForm,
            'hash': 1,
            'opt_general': True,
            'opt_sales': False,
            'opt_new': False
        })

    def post(self, request, pk, *args, **kwargs):
        print(args)
        print(kwargs)
        return HttpResponse("Toto")
