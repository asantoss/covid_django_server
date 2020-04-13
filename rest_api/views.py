import sys
sys.path.append(".")
from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .models import Country, State
from .serializers import CountrySerializer, StateSerializer, LiveSerializer
from rest_framework.decorators import api_view
from .data_sources.worlometer.scraper import Scraper
from rest_framework.response import Response
import json
# Create your views here.


class CountryView(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class StateView(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer


@api_view(['GET'])
def states_live(request):
    states = Scraper('https://www.worldometers.info/coronavirus/country/us/',
                     'usa_table_countries_today', 'states-data',
                     'http://127.0.0.1:8000/api/states')
    serializer = LiveSerializer(states.parse(), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def countries_live(request):
    countries = Scraper('https://www.worldometers.info/coronavirus/',
                        'main_table_countries_today', 'countries-data',
                        'http://127.0.0.1:8000/api/countries')
    seriallizer = LiveSerializer(countries.parse(), many=True)
    # countries.daily_scrape()
    return Response(seriallizer.data)


# @api_view(['POST'])
# def countries_save(request):
#     # seriallizer = LiveSerializer(countries.parse(), many=True)
#     body = request.POST.dict()
#     try:
#         entry = Country(**body)
#         entry.save()
#     except:
#         pass
#     return Response({'message': 'Hello World'})
