import requests


class Client:
    def __init__(self, url: str):
        self.url = url
        self.pipeline_id = None
        self.destination_id = None

    def with_pipeline(self, pipeline_id: int):
        self.pipeline_id = pipeline_id
        return self

    def with_destination(self, destination_id: int):
        self.destination_id = destination_id
        return self

    def search(self, query: str, top_k: int = 1):
        if not self.pipeline_id and not self.destination_id:
            raise TypeError("Missing pipeline or destination, try with_pipeline or with_destination")
        payload = {
            "query": query,
            "top_k": top_k,
            "pipeline_id": self.pipeline_id,
            "destination_id": self.destination_id
        }
        response = requests.post(f"{self.url}/search", json=payload)
        return response

    def generate(self, query: str, top_k: int = 1):
        if not self.pipeline_id and not self.destination_id:
            raise TypeError("Missing pipeline or destination, try with_pipeline or with_destination")
        payload = {
            "query": query,
            "top_k": top_k,
            "pipeline_id": self.pipeline_id,
            "destination_id": self.destination_id
        }
        response = requests.post(f"{self.url}/generate", json=payload)
        return response


