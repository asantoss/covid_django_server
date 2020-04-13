from scraper import Scraper
import os

base_url = os.getenv('APP_URL')

states = Scraper('https://www.worldometers.info/coronavirus/country/us/',
                 'usa_table_countries_today', 'states-data',
                 base_url + 'states/')
states.daily_scrape()

countries = Scraper('https://www.worldometers.info/coronavirus/',
                    'main_table_countries_today', 'countries-data',
                    base_url + 'countries/')
countries.daily_scrape()