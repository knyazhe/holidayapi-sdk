import config
from myholidayapi import *

holidayapi = MyHolidayApi(config.API)

print(holidayapi.get_holidays(country="RU", year=2024))
