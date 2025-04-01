import requests
import json

from myholidayapi.client import HolidayAPIClient
from myholidayapi.countries import Countries
from myholidayapi.holidays import Holidays


class MyHolidayAPI:
    def __init__(self, api_key) -> None:
        self.client = HolidayAPIClient(api_key)
        self.holidays = Holidays(self.client)
        self.countries = Countries(self.client)