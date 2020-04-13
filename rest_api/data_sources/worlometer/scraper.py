from bs4 import BeautifulSoup
import re
import requests
import json
from datetime import datetime
import os


class Scraper:
    data = []

    def __init__(self, url, table, file_name, api):
        self.url = url
        self.table = table
        self.file_name = file_name
        self.lastScrape = 0
        self.api = api

    def parse(self):
        now = datetime.now()
        try:
            if (self.lastScrape == 0
                    or now.timestamp() - self.lastScrape > 60 * 45):
                self.lastScrape = datetime.now().timestamp()
                html = requests.get(self.url)
                soup = BeautifulSoup(html.content, 'html.parser')
                myTable = soup.find(id=self.table)
                headers = myTable.select('thead > tr > th')
                data_rows = myTable.select('tbody > tr')
                file = open(self.file_name + '.json', 'w')
                new_data = []
                for row in data_rows:
                    entry = {}
                    entry['entry_date'] = datetime.now()
                    cols = row.select('td')
                    j = 0
                    for col in cols:
                        header = headers[j].get_text('_', strip=True).replace(
                            '/', '').lower().replace(u'\xa0', 'al_').replace(
                                ' pop', '_pop').replace(',', '')
                        column = re.sub('[+,]', '', col.get_text('',
                                                                 strip=True))

                        if (j == 0):
                            header = 'name'
                        if (j == 1):
                            header = 'total_cases'
                        if (header == 'deaths'):
                            header = 'total_deaths'
                        if (header == 'source'):
                            j += 1
                            continue
                        j += 1
                        entry[header] = column or 0
                    if (entry['name'] and entry['name'] != 'Total:'):
                        new_data.append(entry)
                self.data = new_data
                json.dump(self.data, file, sort_keys=True, default=str)
                return self.data
            else:
                return self.data
        except:
            return 'Could not scrape, data'

    def daily_scrape(self):
        data = self.parse()
        for entry in data:
            r = requests.post(self.api, data=entry)
            print(r.text)
