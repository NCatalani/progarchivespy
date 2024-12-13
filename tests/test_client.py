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


def test_client_top_albums_complex_query_success(client):
    expected_genres = [
        Subgenre.SYMPHONIC_PROG,
        Subgenre.CROSSOVER_PROG,
        Subgenre.KRAUTROCK,
    ]
    expected_years = [1970, 1983, 2003, 2009, 2014]
    expected_result_size = 133
    expected_min_num_ratings = 60
    expected_min_avg_rating = 3.3

    result = client.top_albums.query(
        subgenres=expected_genres,
        min_num_ratings=expected_min_num_ratings,
        min_avg_rating=expected_min_avg_rating,
        years=expected_years,
        max_results=expected_result_size,
    )

    # Check if the result has the expected size
    assert len(result) == expected_result_size

    for i, res in enumerate(result):
        expected_position = i + 1

        # Sanity checks for each result
        assert res.position == expected_position
        assert res.album.genre in expected_genres
        assert res.album.ratings >= expected_min_num_ratings
        assert res.album.score >= expected_min_avg_rating
        assert res.album.year in expected_years
