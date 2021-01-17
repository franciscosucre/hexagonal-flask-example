from dataclasses import field, dataclass
from uuid import uuid4


@dataclass(frozen=True)
class Cat:
    name: str = field()
    id: str = field(default_factory=lambda: str(uuid4()))
