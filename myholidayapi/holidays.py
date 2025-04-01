from myholidayapi.client import HolidayAPIClient
from myholidayapi.utils import clear_params

class Holidays:
    def __init__(self, client: HolidayAPIClient) -> None:
        self.client = client

    def get(self,
                     country: str,
                     year: str,
                     month: int = None,
                     day: int = None,
                     public: bool = None,
                     subdivisions: bool = None,
                     search: str = None,
                     language: str = None,
                     previous: bool = None,
                     upcoming: bool = None,
                     format: str = None,
                     pretty: bool = None) -> dict:
        '''
        :param country:
        :param year:
        :param month:
        :param day:
        :param public:
        :param subdivisions:
        :param search:
        :param language:
        :param previous:
        :param upcoming:
        :param format:
        :param pretty:
        :return: json formatted holidays

        holidays
        '''
        params = {
            "country": country,
            "year": year,
            "month": month,
            "day": day,
            "public": public,
            "subdivisions": subdivisions,
            "search": search,
            "language": language,
            "previous": previous,
            "upcoming": upcoming,
            "format": format,
            "pretty": pretty
        }
        clean_params = clear_params(params)
        response = self.client.request("/holidays", params=clean_params)['holidays']
        return response