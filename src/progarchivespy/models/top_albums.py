from dataclasses import dataclass
from progarchivespy.models import Album, Artist
from progarchivespy.models.serializable import Serializable


@dataclass
class AlbumQueryResult(Serializable):
    position: int
    weighted_score: float
    album: Album
    artist: Artist
