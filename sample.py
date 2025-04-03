
from holidayapi_sdk import HolidayAPI
from holidayapi_sdk.models import *

holidayapi = HolidayAPI("your_api")
query = HolidaysQuery(country="RU", year=2024)
print(holidayapi.holidays.get(query))