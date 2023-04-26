from dataclasses import dataclass
from typing import Optional, List

import requests


@dataclass
class Source:
    id: int


@dataclass
class Destination:
    id: int


@dataclass
class Pipeline:
    id: int
    yaml: str
    sources: List[Source]
    destinations: List[Destination]

    def __init__(self, server, kwargs):
        self.server = server
        self.id = kwargs['pipeline']['id']
        self.yaml = kwargs['pipeline']['yaml']
        self.sources = []
        self.destinations = []
        for record in kwargs['sources']:
            self.sources.append(Source(record['id']))
        for record in kwargs['destinations']:
            self.destinations.append(Destination(record['id']))

    def start(self) -> dict:
        response = requests.post(f"{self.server}/pipeline/start/{self.id}", json={})
        return response.json()

    def stop(self) -> dict:
        response = requests.post(f"{self.server}/pipeline/stop/{self.id}", json={})
        return response.json()

    @property
    def status(self) -> str:
        response = requests.get(f"{self.server}/pipeline/{self.id}", json={})
        return response.json()['status']
