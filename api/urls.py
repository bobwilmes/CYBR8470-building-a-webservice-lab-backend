from django.conf.urls import include, url

#Django Rest Framework
from rest_framework import routers

from api import controllers
from django.views.decorators.csrf import csrf_exempt

#REST API routes
router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    url(r'^api/dogs/$', csrf_exempt(controllers.DogDetail())),
    url(r'^api/dogs/', csrf_exempt(controllers.DogList())),
    url(r'^api/breeds/$', csrf_exempt(controllers.BreedDetail())),
    url(r'^api/breeds/', csrf_exempt(controllers.BreedList())),
    url(r'^', include(router.urls)),
]
