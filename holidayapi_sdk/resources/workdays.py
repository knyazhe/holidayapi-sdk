from holidayapi_sdk.models import WorkdaysQuery
from holidayapi_sdk.resources.base import BaseResource


class Workdays(BaseResource):
    def get(self, query: WorkdaysQuery) -> dict:
        """
        Calculates the number of workdays (based on country's workweek) that occur between a given date range.

        Args:
            query (WorkdaysQuery): параметры запроса

        Returns:
            dict: Number of working / business days between the specified start and end dates
        """
        return self._get("/workdays", query.to_query())