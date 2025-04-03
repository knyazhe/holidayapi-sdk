from holidayapi_sdk.models import WorkdayQuery
from holidayapi_sdk.resources.base import BaseResource


class Workday(BaseResource):
    def get(self, query: WorkdayQuery) -> dict:
        """
        Calculates the workday (based on country's workweek) that occurs a given number of days after a date.

        Args:
            query (WorkdayQuery): параметры запроса

        Returns:
            dict: date The date of the calculated workday. weekday Day of the week that the workday occurs.
        """
        return self._get("/workday", query.to_query())