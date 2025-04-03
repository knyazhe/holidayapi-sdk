import requests
import json

class HolidayAPIClient:
    '''
    Клиент
    '''
    def __init__(self, key: str, api_url: str ="https://holidayapi.com/v1") -> None:
        '''

        :param key: API ключ
        :param api_url: url до API
        '''
        self.__api_key = key
        self.__api_url = api_url
        self.session = requests.Session()

    def request(self, endpoint: str, params: dict = None) -> dict:
        if params is None:
            params = {}
        url = self.__api_url + endpoint
        params["key"] = self.__api_key
        response = self.session.get(url, params=params)

        if response.status_code == 200:
            json_response = response.json()
            if json_response['status'] != 200:
                raise Exception(json_response['error'])
        else:
            raise Exception(response.status_code, response.text)

        return response.json()