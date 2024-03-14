from dataclasses import dataclass

@dataclass
class Task:
    id: int
    name: str
    graph: dict
    ontology: dict
    text: dict
