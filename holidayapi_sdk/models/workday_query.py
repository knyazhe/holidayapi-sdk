
from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class WorkdayQuery(BaseModel):
    country: str = Field(None, description="For country code")
    start: date = Field(None,description="The date (in YYYY-MM-DD format) from which to begin counting.")
    days: int = Field(None,description="Number of working / business days to advance (positive integer) or retrogress (negative integer) from start.")

    format: Optional[str] = Field(None, description="Response format (csv, json, php, tsv, yaml, xml). Defaults to JSON.")
    pretty: Optional[bool] = Field(None, description="Prettify the output for humans.")

    def to_query(self) -> dict:
        """Transform query to dictionary"""
        query = self.model_dump(exclude_none=True)
        return query