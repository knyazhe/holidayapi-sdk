from myholidayapi.client import HolidayAPIClient
from myholidayapi.countries import Countries
from myholidayapi.holidays import Holidays
from myholidayapi.languages import Languages
from myholidayapi.workday import Workday
from myholidayapi.workdays import Workdays


class MyHolidayAPI:
    def __init__(self, api_key) -> None:
        self.client = HolidayAPIClient(api_key)
        self.holidays = Holidays(self.client)
        self.countries = Countries(self.client)
        self.languages = Languages(self.client)
        self.workday = Workday(self.client)
        self.workdays = Workdays(self.client)