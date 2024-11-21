import pytest
from progarchivespy import ProgArchivesClient
from progarchivespy.common.http import BaseHTTPClient
from progarchivespy.common.definitions import Subgenre


# Fixture with client
@pytest.fixture
def client():
    return ProgArchivesClient()


def test_client_default_http_client(client):
    assert isinstance(client.top_albums.http_client, BaseHTTPClient)


def test_client_top_albums_by_genre_success(client):
    expected_genre = Subgenre.SYMPHONIC_PROG
    expected_result_size = 77
    expected_min_num_ratings = 20

    result = client.top_albums.query(
        subgenres=[expected_genre],
        min_num_ratings=expected_min_num_ratings,
        max_results=expected_result_size,
    )

    assert len(result) == expected_result_size

    for i, res in enumerate(result):
        expected_position = i + 1

        assert res.album.genre == expected_genre
        assert res.position == expected_position
        assert res.album.ratings >= expected_min_num_ratings
