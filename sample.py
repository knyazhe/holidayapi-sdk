import config
from myholidayapi import MyHolidayAPI

holidayapi = MyHolidayAPI(config.API)

# print(holidayapi.holidays.get(country="RU", year="2024"))

print(holidayapi.countries.get())
