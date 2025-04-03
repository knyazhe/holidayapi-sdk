
from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class WorkdaysQuery(BaseModel):
    """
        Query model for the /workdays endpoint of HolidayAPI.

        Allows specifying the country and date range for counting workdays between two dates.

        Attributes:
            country (str): Country code to calculate workdays for (e.g., "RU").
            start (date): The start date (in YYYY-MM-DD format) from which to begin counting.
            end (date): The end date (in YYYY-MM-DD format) to count until.
            format (str, optional): Response format (csv, json, php, tsv, yaml, xml). Defaults to JSON.
            pretty (bool, optional): If True, prettifies the output for human readability.
    """
    country: str = Field(None, description="For country code")
    start: date = Field(None,description="The date (in YYYY-MM-DD format) from which to begin counting.")
    end: date = Field(None,description="The date (in YYYY-MM-DD format) to count until.")

    format: Optional[str] = Field(None, description="Response format (csv, json, php, tsv, yaml, xml). Defaults to JSON.")
    pretty: Optional[bool] = Field(None, description="Prettify the output for humans.")

    def to_query(self) -> dict:
        """Transform query to dictionary
        :returns: dict
        """
        query = self.model_dump(exclude_none=True)
        return query
