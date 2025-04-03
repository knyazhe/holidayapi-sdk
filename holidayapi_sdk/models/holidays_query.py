from pydantic import BaseModel, Field
from typing import Optional

class HolidaysQuery(BaseModel):
    """
    Query model for the /holidays endpoint of HolidayAPI.

    Allows filtering holiday data using various parameters.

    Attributes:
        country (str): Country code (e.g., 'RU'). Required.
        year (int): Year to query (e.g., 2024). Required.
        month (int, optional): Month (1–12).
        day (int, optional): Day of the month (1–31).
        public (bool, optional): Return only public holidays.
        subdivisions (bool, optional): Include state/province holidays.
        search (str, optional): Search holidays by name (min 5 characters).
        language (str, optional): Language code (e.g., 'en').
        previous (bool, optional): Return first holiday before specified date (requires month and day).
        upcoming (bool, optional): Return first holiday after specified date (requires month and day).
        format (str, optional): Response format: csv, json, php, tsv, yaml, xml (default is json).
        pretty (bool, optional): Prettify the output for readability.
    """

    country: str = Field(..., description="Country code, e.g., 'RU'")
    year: int = Field(..., ge=1, description="Year to query, e.g., 2024")
    month: Optional[int] = Field(None, ge=1, le=12, description="Optional month")
    day: Optional[int] = Field(None, ge=1, le=31, description="Optional day")
    public: Optional[bool] = Field(None, description="Filter for public holidays only")
    subdivisions: Optional[bool] = Field(None, description="Return state / province holidays alongside countrywide holidays")
    search: Optional[str] = Field(None, description="Search holidays by name. Minimum 5 characters.")
    language: Optional[str] = Field(None, description="Language code, e.g., 'en'")
    previous: Optional[bool] = Field(None, description="Return the first day of holidays that occur before the specific date. month and day are required. Cannot be used with upcoming.")
    upcoming: Optional[bool] = Field(None, description="Return the first day of holidays that occur after the specific date. month and day are required. Cannot be used with previous.")
    format: Optional[str] = Field(None, description="Response format (csv, json, php, tsv, yaml and xml). Defaults to JSON")
    pretty: Optional[bool] = Field(None, description="Prettifies results to be more human-readable")

    def to_query(self) -> dict:
        """
        Transform query to dictionary
        """
        query = self.model_dump(exclude_none=True)
        return query
