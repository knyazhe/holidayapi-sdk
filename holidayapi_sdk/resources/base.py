class BaseResource:
    def __init__(self, client):
        self.client = client

    def _get(self, endpoint: str, params: dict) -> dict:
        return self.client.request(endpoint, params)