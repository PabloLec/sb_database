import dataclasses
from datetime import datetime


@dataclasses.dataclass
class User:
    id: int
    username: str
    password: str
    email: str
    created_at: datetime
