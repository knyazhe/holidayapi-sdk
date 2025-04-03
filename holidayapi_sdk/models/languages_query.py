
from pydantic import BaseModel, Field
from typing import Optional

class LanguagesQuery(BaseModel):
    country: Optional[str] = Field(None, description="Filter by specific country code.")
    search: Optional[str] = Field(None, min_length=2, description="Search by code or name (min 2 characters).")
    public: Optional[bool] = Field(None, description="Only return countries with public holidays.")
    format: Optional[str] = Field(None, description="Response format (csv, json, php, tsv, yaml, xml). Defaults to JSON.")
    pretty: Optional[bool] = Field(None, description="Prettify the output for humans.")

    def to_query(self) -> dict:
        """Transform query to dictionary"""
        query = self.model_dump(exclude_none=True)
        return query
