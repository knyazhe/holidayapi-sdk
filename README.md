# holidayapi-alt

**Unofficial Python SDK for [HolidayAPI](https://holidayapi.com)** 

> This project is an independent alternative to the [official SDK](https://github.com/holidayapi/holidayapi-python).

---

## Quick Example

```python
from holidayapi import HolidayAPI
from holidayapi.models import HolidayQuery

api = HolidayAPI("your_api_key")

query = HolidayQuery(country="US", year=2024)
response = api.holidays.get_holidays(query)

print(response)
