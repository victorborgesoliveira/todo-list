from dataclasses import dataclass
from datetime import datetime

@dataclass(slots=True)
class Task:
    description: str
    status: str
    created_at: datetime

    def __init__(self, description: str, status: str, created_at: datetime):
        self.status = status
        self.description = description
        self.created_at = created_at