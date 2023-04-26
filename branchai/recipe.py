import requests

from branchai.pipeline import Pipeline


class Recipe:
    server_url = ""
    payload = {}

    def __init__(self, server_url, template: str):
        self.server_url = server_url
        if template == "webpage":
            self.url = f"{self.server_url}/recipes/webpage"
        else:
            raise TypeError(f"Recipe ({template}) not supported")

    def create_pipeline(self, payload: dict) -> Pipeline:
        if 'source' not in payload:
            raise TypeError("source parameter missing")
        if 'destination' not in payload:
            raise TypeError("destination parameter missing")
        response = requests.post(self.url, json=payload)
        if response.status_code == 200:
            return Pipeline(self.server_url, response.json())
        else:
            raise TypeError("Unable to create pipeline")
