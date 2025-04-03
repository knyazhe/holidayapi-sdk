from holidayapi_sdk.client import HolidayAPIClient
from holidayapi_sdk.resources.countries import Countries
from holidayapi_sdk.resources.holidays import Holidays
from holidayapi_sdk.resources.languages import Languages
from holidayapi_sdk.resources.workday import Workday
from holidayapi_sdk.resources.workdays import Workdays


class HolidayAPI:
    def __init__(self, api_key) -> None:
        self.client = HolidayAPIClient(api_key)

        self.holidays = Holidays(self.client)
        self.countries = Countries(self.client)
        self.languages = Languages(self.client)
        self.workday = Workday(self.client)
        self.workdays = Workdays(self.client)