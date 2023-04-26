from branchai.adapter import Adapter
from branchai.recipe import Recipe


class Client:
    def __init__(self, server_url: str):
        self.server_url = server_url

    def with_adapter(self, pipeline_id: int, destination_id: int = None) -> Adapter:
        return Adapter(self.server_url, pipeline_id=pipeline_id, destination_id=destination_id)

    def with_recipe(self, template: str) -> Recipe:
        return Recipe(self.server_url, template)
