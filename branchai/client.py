import requests

from branchai import Adapter, Recipe


class Client:
    def __init__(self, url: str):
        self.url = url

    def with_adapter(self, pipeline_id: int, destination_id: int = None) -> Adapter:
        return Adapter(self.url, pipeline_id=pipeline_id, destination_id=destination_id)

    def with_recipe(self, template: str, payload: dict) -> Recipe:
        return Recipe.create(template, payload)
