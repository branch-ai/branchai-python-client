from typing import Optional

import requests

from branchai.adapter import Adapter
from branchai.recipe import Recipe




class Client:
    def __init__(self, server_url: str, api_token: Optional[str] = None):
        self.server_url = server_url
        self.headers = {}
        if api_token:
            self.headers['Authorization'] = f"Bearer {api_token}"

    def with_adapter(self, pipeline_id: int, destination_id: int = None) -> Adapter:
        return Adapter(self.server_url, pipeline_id=pipeline_id, destination_id=destination_id, headers=self.headers)

    def with_recipe(self, template: str) -> Recipe:
        return Recipe(self.server_url, template)
