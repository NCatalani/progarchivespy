import pytest
import requests
from unittest.mock import MagicMock, patch

from progarchivespy.common.http import BaseHTTPClient


# Fixtures
@pytest.fixture
def mock_response():
    """Fixture for a mock requests.Response object."""
    return MagicMock(spec=requests.Response)


@pytest.fixture
def mock_session(mock_response):
    """Fixture for a mock requests.Session object."""
    session = MagicMock(spec=requests.Session)
    session.request.return_value = mock_response
    return session


@pytest.fixture
def client_with_session(mock_session):
    """Fixture for BaseHTTPClient initialized with a mock session."""
    return BaseHTTPClient(session=mock_session)


@pytest.fixture
def client_without_session():
    """Fixture for BaseHTTPClient without a session."""
    return BaseHTTPClient()


# Tests
def test_make_request_with_session(client_with_session, mock_session, mock_response):
    """
    Test that the `make_request` method uses the provided session.
    """
    response = client_with_session.make_request("GET", "http://example.com")

    mock_session.request.assert_called_once_with(
        "GET",
        "http://example.com",
        headers=BaseHTTPClient.BASE_HEADERS,
    )
    assert response == mock_response


def test_make_request_without_session(client_without_session, mock_response):
    """
    Test that the `make_request` method uses `requests.request` directly
    when no session is provided.
    """
    with patch("requests.request", return_value=mock_response) as mock_request:
        response = client_without_session.make_request("GET", "http://example.com")

        mock_request.assert_called_once_with(
            "GET",
            "http://example.com",
            headers=BaseHTTPClient.BASE_HEADERS,
        )
        assert response == mock_response


def test_make_request_with_custom_headers(client_with_session, mock_session):
    """
    Test that the `make_request` method merges custom headers with the default headers.
    """
    custom_headers = {"Authorization": "Bearer token123"}
    client_with_session.make_request(
        "POST", "http://example.com", headers=custom_headers
    )

    expected_headers = BaseHTTPClient.BASE_HEADERS | custom_headers
    mock_session.request.assert_called_once_with(
        "POST",
        "http://example.com",
        headers=expected_headers,
    )


def test_get_method(client_without_session, mock_response):
    """
    Test the `get` method calls `make_request` with method "GET".
    """
    with patch("requests.request", return_value=mock_response) as mock_request:
        response = client_without_session.get(
            "http://example.com", params={"q": "search"}
        )

        mock_request.assert_called_once_with(
            "GET",
            "http://example.com",
            params={"q": "search"},
            headers=BaseHTTPClient.BASE_HEADERS,
        )
        assert isinstance(response, requests.Response)
