from dataclasses import dataclass
from progarchivespy.common.definitions import AlbumType, Subgenre


# Columns
@dataclass
class PositionColumn:
    """
    Dataclass for the position column in the top albums table.

    Attributes:
        position (int): The position of the album in the table.
    """

    position: int


@dataclass
class CoverColumn:
    """
    Dataclass for the cover column in the top albums table.

    Attributes:
        url (str): The URL of the album's cover.
    """

    url: str


@dataclass
class RatingColumn:
    """
    Dataclass for the rating column in the top albums table.

    Attributes:
        score (float): The score of the album.
        ratings (int): The number of ratings the album has received.
        weighted_rating (float): The weighted rating of the album.
    """

    score: float
    ratings: int
    weighted_rating: float


@dataclass
class SummaryColumn:
    """
    Dataclass for the summary column in the top albums table.

    Attributes:
        artist_id (int): The ID of the artist.
        artist_name (str): The name of the artist.
        album_id (int): The ID of the album.
        album_name (str): The name of the album.
    """

    artist_id: int
    artist_name: str
    album_id: int
    album_name: str


@dataclass
class GenreColumn:
    """
    Dataclass for the genre column in the top albums table.

    Attributes:
        genre (Subgenre): The subgenre of the album.
        album_type (AlbumType): The type of the album.
        release_year (int): The release year of the album.
    """

    genre: Subgenre
    album_type: AlbumType
    release_year: int


# Row
@dataclass
class AlbumTableRow:
    """
    Dataclass for a row in the top albums table.

    Attributes:
        position (PositionColumn)
        cover (CoverColumn)
        rating (RatingColumn)
        summary (SummaryColumn)
        genre (GenreColumn)
    """

    position: PositionColumn
    cover: CoverColumn
    rating: RatingColumn
    summary: SummaryColumn
    genre: GenreColumn


# Page / Table
@dataclass
class AlbumTable:
    """
    Dataclass for a page in the top albums table.

    Attributes:
        rows (list[AlbumTableRow]): The list of rows in the table.
    """

    rows: list[AlbumTableRow]
