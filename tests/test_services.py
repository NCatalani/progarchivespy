import pytest

from unittest.mock import MagicMock
from progarchivespy.services import TopAlbumsService
from progarchivespy.common.exceptions import ParseException
from progarchivespy.common.definitions import (
    PROGARCHIVES_BASE_URL,
    Subgenre,
    Country,
    AlbumType,
)


# Fixtures
@pytest.fixture
def mock_http_client():
    """Fixture for a mocked HTTP client."""
    return MagicMock()


@pytest.fixture
def top_albums_service(mock_http_client):
    """Fixture for the TopAlbumsService with a mocked HTTP client."""
    return TopAlbumsService(http_client=mock_http_client)


@pytest.fixture
def sample_html_file():
    """Fixture to load the sample HTML file."""
    with open(
        "tests/data/top_symphonic_prog_albums.html", "r", encoding="utf-8"
    ) as file:
        return file.read()


# Tests
def test_parse_response_with_sample_file(top_albums_service, sample_html_file):
    """
    Test the parse_response method with dynamically loaded sample HTML.
    """
    results = top_albums_service.parse_response(sample_html_file)

    assert len(results) > 0
    first_result = results[0]

    assert first_result.album.name  # Ensure album name exists
    assert first_result.artist.name  # Ensure artist name exists


def test_empty_query_with_sample_file(
    top_albums_service, mock_http_client, sample_html_file
):
    """
    Test the query method using the sample HTML file as the mock response.
    """
    # Mock the HTTP response
    mock_response = MagicMock()
    mock_response.text = sample_html_file
    mock_response.raise_for_status = MagicMock()
    mock_http_client.get.return_value = mock_response

    # Perform the query
    results = top_albums_service.query()

    # Assert HTTP client was called with correct parameters
    mock_http_client.get.assert_called_once_with(
        f"{PROGARCHIVES_BASE_URL}/top-prog-albums.asp", params={"smaxresults": "100"}
    )

    # Basic assertions (adjust based on the sample HTML content)
    assert len(results) == 100

    first_result = results[0]
    assert first_result.album.name  # Ensure album name exists
    assert first_result.artist.name  # Ensure artist name exists


def test_full_query_with_sample_file(
    top_albums_service, mock_http_client, sample_html_file
):
    """
    Test the query method using the sample HTML file as the mock response.
    """
    # Mock the HTTP response
    mock_response = MagicMock()
    mock_response.text = sample_html_file
    mock_response.raise_for_status = MagicMock()
    mock_http_client.get.return_value = mock_response

    # Perform the query
    results = top_albums_service.query(
        subgenres=[Subgenre.SYMPHONIC_PROG],
        countries=[Country.UNITED_KINGDOM],
        album_types=[AlbumType.STUDIO],
        years=[1973],
        min_avg_rating=3.5,
        min_num_ratings=20,
        max_num_ratings=40000,
        max_results=10,
    )

    # Assert HTTP client was called with correct parameters
    mock_http_client.get.assert_called_once_with(
        f"{PROGARCHIVES_BASE_URL}/top-prog-albums.asp",
        params={
            "ssubgenres": str(Subgenre.SYMPHONIC_PROG.id),
            "scountries": str(Country.UNITED_KINGDOM.id),
            "salbumtypes": str(AlbumType.STUDIO.id),
            "syears": "1973",
            "sminavgrating": "3.5",
            "sminnumratings": "20",
            "smaxnumratings": "40000",
            "smaxresults": "10",
        },
    )

    # Basic assertions (adjust based on the sample HTML content)
    assert len(results) > 0
    first_result = results[0]

    assert first_result.album.name  # Ensure album name exists
    assert first_result.artist.name  # Ensure artist name exists


def test_parse_response_with_broken_html(top_albums_service):
    """
    Test that parse_response raises an exception when the HTML structure is broken.
    """
    # Simulate broken HTML
    broken_html = """
    <html>
        <body>
            <table></table>
            <table>
                <tr>
                    <td><strong>1</strong></td>
                    <td><img src="cover1.jpg" /></td>
                    <!-- Missing other columns -->
                </tr>
            </table>
        </body>
    </html>
    """

    # Assert that an exception is raised
    with pytest.raises(ParseException, match="Non-standard table row"):
        top_albums_service.parse_response(broken_html)

    broken_html = """
    <html>
        <body>
            <table></table>
        </body>
    </html>
    """

    # Assert that an exception is raised
    with pytest.raises(ParseException, match="Non-standard page"):
        top_albums_service.parse_response(broken_html)
