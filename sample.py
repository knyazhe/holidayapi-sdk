from holidayapi_sdk import HolidayAPI
from holidayapi_sdk.models.holidays_query import HolidaysQuery

api = HolidayAPI('API_KEY')

query = HolidaysQuery(
    country="RU",
    year=2024,
    pretty=True
)

response = api.holidays.get(query)
holidays = response['holidays']
print(f'Holidays in {query.country}, in {query.year} year\n')
for holiday in holidays:
    print(f'Holiday: {holiday['name']} \ndate: {holiday["date"]}\n')