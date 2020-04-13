from rest_framework import serializers
from .models import Country, State


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class LiveSerializer(serializers.Serializer):
    name = serializers.CharField()
    total_cases = serializers.IntegerField()
    new_cases = serializers.IntegerField()
    total_deaths = serializers.IntegerField()
    new_deaths = serializers.IntegerField()
    active_cases = serializers.IntegerField()
    total_cases_1m_pop = serializers.FloatField()
    deaths_1m_pop = serializers.FloatField()
    tests_1m_pop = serializers.FloatField()
    total_tests = serializers.IntegerField()
    entry_date = serializers.DateTimeField()
    continent = serializers.CharField()
