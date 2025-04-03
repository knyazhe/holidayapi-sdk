from holidayapi_sdk.models import HolidaysQuery
from holidayapi_sdk.resources.base import BaseResource


class Holidays(BaseResource):
    def get(self, query: HolidaysQuery) -> dict:
        """
        Retrieves a list public holidays and observances for countries, states and provinces.

        Args:
            query (HolidayQuery): параметры запроса

        Returns:
            dict: список праздников из API
        """
        return self._get("/holidays", query.to_query())