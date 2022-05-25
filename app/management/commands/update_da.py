from datetime import timedelta, datetime
from random import randint

from django.core.management import BaseCommand
import xml.etree.ElementTree as ET

from app.models import GoogleSheets
import requests


class Command(BaseCommand):
    google_sheets_objects = []

    def handle(self, *args, **options):
        # update cb
        url_crb = 'http://www.cbr.ru/scripts/XML_daily.asp'
        rez = requests.get(url_crb)

        myroot = ET.fromstring(rez.text)
        for valute in myroot.findall('Valute'):
            if valute.find('CharCode').text == 'USD':
                usd = valute.find('Value').text
                usd = float(usd.replace(',', '.'))
                break

        # update sheet
        with open('test_google.csv', 'r') as file:
            info = file.readlines()[1:]
        google_sheets = [line.strip().split(',')for line in info]
        # update db
        # google_sheets = GoogleSheets.objects.all()
        for row in google_sheets:
            self.google_sheets_objects.append(
                GoogleSheets(
                    id=int(row[0]),
                    order=int(row[1]),
                    price_dollar=float(row[2]),
                    price_ruble=float(row[2]),
                    delivery_time=datetime(row[3]),
                ))
        # GoogleSheets.objects

        # cronfile
        # dockerfile crontab cronfile
        # docker python3 manage.py run_server

        return self.style.SUCCESS('DONE')
