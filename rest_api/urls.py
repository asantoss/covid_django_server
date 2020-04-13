from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('countries', views.CountryView)

router.register('states', views.StateView)

urlpatterns = [
    path('', include(router.urls)),
    path('states-live', views.states_live),
    path('countries-live', views.countries_live),
]
