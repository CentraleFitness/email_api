from django.conf.urls import url, include
from django.contrib.auth.models import User
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets
from rest_framework_swagger.views import get_swagger_view
from emailapp import views

swagger_view = get_swagger_view(title='Email API')


urlpatterns = [
    url(r'^docs/$', swagger_view, name='docs'),
    url(r'^proximity/$', views.ProximityAlertAPI.as_view()),
    url(r'^newsletter/recipient/$',
        views.NewsletterRecipientAPI.as_view()),
    url(r'^newsletter/recipient/list/$',
        views.NewsletterRecipientListAPI.as_view()),
    url(r'^newsletter/recipient/(?P<pk>\d+)/unsubscribe/$',
        views.NewsletterUnsubscribeAPI.as_view()),
    url(r'^newsletter/recipient/(?P<pk>\d+)/manage/$',
        views.ManageView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
