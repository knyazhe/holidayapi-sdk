from holidayapi_sdk.models import CountriesQuery
from holidayapi_sdk.resources.base import BaseResource


class Countries(BaseResource):
    """Class Countries contains method get"""
    def get(self, query: CountriesQuery) -> dict:
        """
        Retrieves a list countries with states and provinces.

        Args:
            query (CountriesQuery): параметры запроса

        Returns:
            dict: список стран
        """
        return self._get("/countries", query.to_query())