from dataclasses import dataclass
from progarchivespy.common.definitions import AlbumType, Subgenre
from progarchivespy.models import Serializable


@dataclass
class Album(Serializable):
    id: int
    name: str
    score: float
    ratings: int
    cover: str
    year: int
    genre: Subgenre
    type: AlbumType
