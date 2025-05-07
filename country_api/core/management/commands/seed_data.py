import requests
from datetime import datetime
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from django.utils import timezone
from ...models import CountryData
from django.conf import settings

class Command(BaseCommand):
    help = 'Seed Data from Country API'

    def handle(self, *args, **kwargs):
        response = requests.get(settings.API_URL)

        if response.status_code == 200:
            data = response.json()
            for a_country in data:
                try:
                    countrydata = CountryData(common_name = a_country["name"]["common"], official_name = a_country["name"]["official"], cca2_name = a_country["cca2"], region = a_country["region"], latitude = a_country["latlng"][0], longitude = a_country["latlng"][1], area = a_country["area"], population = a_country["population"], flag = a_country["flags"]["png"], timezones = a_country["timezones"], full_response = a_country, updated_by = None, updated_at = timezone.now())
                    subregion = ""
                    if "subregion" in a_country:
                        subregion = a_country["subregion"]
                    capital = ""
                    if "capital" in a_country:
                        capital = ", ".join(a_country["capital"])
                    languages = []
                    if "languages" in a_country:
                        for key, value in a_country["languages"].items():
                            languages.append(value)
                    countrydata.capital = capital
                    countrydata.languages = languages
                    countrydata.subregion = subregion
                    countrydata.save()
                except IntegrityError:
                    self.stdout.write(self.style.ERROR(f'Data of ${a_country["name"]["common"]} already exists'))
                except Exception as e:
                    print(e)
                    self.stdout.write(self.style.ERROR(f'Could not save data of ${a_country["name"]["common"]}'))
            self.stdout.write(self.style.SUCCESS('Data seeded successfully!'))
        else:
            self.stdout.write(self.style.ERROR('Could not load data'))
