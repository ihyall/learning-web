from dataclasses import dataclass
from datetime import datetime
from .task import Task

@dataclass
class Answer:
    task_id: int
    user_id: int
    date: datetime
    data: Task
