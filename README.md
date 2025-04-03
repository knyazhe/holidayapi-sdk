# holidayapi-sdk

A clean, modular and typed Python SDK for HolidayAPI (https://holidayapi.com).  
Provides a structured interface to access holidays, countries, languages, workdays, and workday endpoints.

***This is an unofficial SDK and is not affiliated with HolidayAPI.***

---

## Installation

Install directly from GitHub:

pip install git+https://github.com/your-username/holidayapi-sdk.git

Or clone the repository manually.

---

## Usage
```python
from holidayapi_sdk import HolidayAPI
from holidayapi_sdk.models.holidays_query import HolidaysQuery

api = HolidayAPI("your_api_key")

query = HolidaysQuery(
    country="RU",
    year=2024,
    pretty=True
)

response = api.holidays.get(query)
print(response)
```
---

## Features

- Resource-based SDK (.holidays, .countries, .languages, .workdays, .workday)
- Request models powered by pydantic
- Explicit .get() method per resource
- Query serialization via .to_query()
- Designed for simplicity and clarity

---

## Roadmap

- [ ] Async support (HolidayAPIAsync)
- [ ] Typed response models (instead of raw dict)
- [ ] Custom exception classes
- [ ] Unit and integration test suite
- [ ] PyPI packaging and release
- [ ] Docs generation 

---

## License

MIT License. See LICENSE for full details.
