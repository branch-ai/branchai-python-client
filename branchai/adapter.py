import requests


class Adapter:
    def __init__(self, server_url, pipeline_id=None, destination_id=None):
        self.server_url = server_url
        self.pipeline_id = pipeline_id
        self.destination_id = destination_id

    def search(self, query: str, top_k: int = 1):
        if not self.pipeline_id and not self.destination_id:
            raise TypeError("Missing pipeline or destination, try with_pipeline or with_destination")
        payload = {
            "query": query,
            "top_k": top_k,
            "pipeline_id": self.pipeline_id,
            "destination_id": self.destination_id
        }
        response = requests.post(f"{self.server_url}/search", json=payload)
        return response

    def generate(self, query: str, top_k: int = 1, system_prompt: str = None, temperature: float = 0, session_id: str = None):
        if not self.pipeline_id and not self.destination_id:
            raise TypeError("Missing pipeline or destination, try with_pipeline or with_destination")
        payload = {
            "query": query,
            "system_prompt": system_prompt,
            "top_k": top_k,
            "temperature": temperature,
            "pipeline_id": self.pipeline_id,
            "destination_id": self.destination_id,
            "session_id": self.session_id
        }
        response = requests.post(f"{self.server_url}/generate", json=payload)
        return response
