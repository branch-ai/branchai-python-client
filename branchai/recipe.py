import requests


class Recipe:
    endpoint = ""
    payload = {}

    @classmethod
    def create(cls, url, template: str, payload: dict):
        if 'source' not in payload:
            raise TypeError("source parameter missing")
        if 'destination' not in payload:
            raise TypeError("destination parameter missing")
        if template == "webpage":
            return WebpageRecipe(url, payload)

    @classmethod
    def create_pipeline(cls, recipe: "Recipe") -> dict:
        response = requests.post(f"{recipe.url}/{recipe.endpoint}", json=recipe.payload)
        if response.status_code == 200:
            return response.json()
        else:
            raise TypeError("Unable to create pipeline")


class WebpageRecipe(Recipe):
    endpoint = "recipes/webpage"

    def __init__(self, url, payload):
        self.payload = payload
        self.url = f"{url}/{self.endpoint}"
        # ToDo: Additional validation for source
