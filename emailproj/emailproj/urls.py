from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework_swagger.views import get_swagger_view

swagger_view = get_swagger_view(title='Email API')


urlpatterns = [
    url(r'docs/$', swagger_view, name='docs'),
]
