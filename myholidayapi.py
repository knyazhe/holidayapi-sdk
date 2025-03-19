import requests
import json

class MyHolidayApi:
    def __init__(self, key):
        self.__key = key

    def get_holidays(self,
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
                    pretty: bool = None):
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

        lalalalallala
        '''
        url = "https://holidayapi.com/v1/holidays"
        params = {"country": country, "key": self.__key, "year": year}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            json_response = response.json()
            if json_response['status'] == 200:
                pass
            else:
                raise Exception(json_response['error'])
            return json_response
        else:
            raise Exception(response.status_code)