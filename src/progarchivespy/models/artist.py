from dataclasses import dataclass, field
from progarchivespy.models import Album, Serializable


@dataclass
class Artist(Serializable):
    id: int
    name: str
    albums: list[Album] = field(default_factory=list)
