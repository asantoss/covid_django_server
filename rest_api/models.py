from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    total_cases = models.IntegerField()
    new_cases = models.IntegerField()
    total_deaths = models.IntegerField()
    new_deaths = models.IntegerField()
    active_cases = models.IntegerField()
    serious_critical = models.IntegerField()
    total_cases_1m_pop = models.FloatField()
    deaths_1m_pop = models.FloatField()
    entry_date = models.CharField(max_length=50)
    total_tests = models.IntegerField()
    continent = models.CharField(max_length=50)
    tests_1m_pop = models.CharField(max_length=50)
    total_recovered = models.IntegerField()


class State(models.Model):
    name = models.CharField(max_length=100)
    total_cases = models.IntegerField()
    new_cases = models.IntegerField()
    total_deaths = models.IntegerField()
    new_deaths = models.IntegerField()
    active_cases = models.IntegerField()
    total_cases_1m_pop = models.FloatField()
    deaths_1m_pop = models.FloatField()
    entry_date = models.CharField(max_length=50)
    total_tests = models.IntegerField()
    tests_1m_pop = models.CharField(max_length=50)
