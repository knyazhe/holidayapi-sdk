from holidayapi_sdk.models import LanguagesQuery
from holidayapi_sdk.resources.base import BaseResource


class Languages(BaseResource):
    def get(self, query: LanguagesQuery) -> dict:
        """
        Retrieves a list languages.

        Args:
            query (HolidayQuery): параметры запроса

        Returns:
            dict: список праздников из API
        """
        return self._get("/languages", query.to_query())