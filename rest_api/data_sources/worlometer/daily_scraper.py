from scraper import Scraper

states = Scraper('https://www.worldometers.info/coronavirus/country/us/',
                 'usa_table_countries_today', 'states-data',
                 'http://127.0.0.1:8000/api/states/')
states.daily_scrape()

countries = Scraper('https://www.worldometers.info/coronavirus/',
                    'main_table_countries_today', 'countries-data',
                    'http://127.0.0.1:8000/api/countries/')
countries.daily_scrape()