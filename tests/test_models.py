import pytest
from progarchivespy.models import AlbumQueryResult, Artist, Album
from progarchivespy.common import Subgenre, AlbumType


@pytest.fixture
def artist():
    return Artist(id=1, name="Artist")


@pytest.fixture
def album():
    return Album(
        id=1,
        name="Album Name",
        ratings=200,
        score=4.5,
        cover="https://example",
        year=2021,
        genre=Subgenre.SYMPHONIC_PROG,
        type=AlbumType.STUDIO,
    )


@pytest.fixture
def album_query_result(artist, album):
    return AlbumQueryResult(position=1, weighted_score=4.5, album=album, artist=artist)


def test_artist_serialize(artist):
    expected = {"id": 1, "name": "Artist", "albums": []}
    assert artist.asdict == expected


def test_album_serialize(album):
    expected = {
        "id": 1,
        "name": "Album Name",
        "ratings": 200,
        "score": 4.5,
        "cover": "https://example",
        "year": 2021,
        "genre": {
            "id": Subgenre.SYMPHONIC_PROG.id,
            "name": Subgenre.SYMPHONIC_PROG.name,
        },
        "type": {
            "id": AlbumType.STUDIO.id,
            "name": AlbumType.STUDIO.name,
        },
    }

    assert album.asdict == expected


def test_album_query_result_serialize(album_query_result):
    expected = {
        "position": 1,
        "weighted_score": 4.5,
        "album": {
            "id": 1,
            "name": "Album Name",
            "ratings": 200,
            "score": 4.5,
            "cover": "https://example",
            "year": 2021,
            "genre": {
                "id": Subgenre.SYMPHONIC_PROG.id,
                "name": Subgenre.SYMPHONIC_PROG.name,
            },
            "type": {
                "id": AlbumType.STUDIO.id,
                "name": AlbumType.STUDIO.name,
            },
        },
        "artist": {"id": 1, "name": "Artist", "albums": []},
    }
    assert album_query_result.asdict == expected
