import requests
from typing import Protocol
from progarchivespy.common import logger


class HTTPClient(Protocol):  # pragma: no cover
    """
    Protocol for HTTP clients compliant with Requests.
    """

    def make_request(self, method: str, url: str, **kwargs) -> requests.Response:
        """Performs an HTTP request."""
        ...

    def get(self, url: str, **kwargs) -> requests.Response:
        """Performs a GET request."""
        ...


class BaseHTTPClient:
    """
    A basic HTTP client leveraging Requests to perform HTTP requests with
    a common set of headers needed for web scraping.
    """

    BASE_HEADERS: dict = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        )
    }

    def __init__(self, session: requests.Session | None = None):
        """
        Initialize the HTTP client.

        Args:
            session (requests.Session | None): Optional request's Session object. Defaults to None.
        """
        self.session = session

    def make_request(self, method: str, url: str, **kwargs) -> requests.Response:
        """
        Performs an HTTP request.

        If a session was provided during initialization, it will be used.
        If not, requests will be stateless.

        Args:
            method (str): HTTP method.
            url (str): URL to request.

        Returns:
            requests.Response: Response object.
        """
        headers: dict = BaseHTTPClient.BASE_HEADERS | kwargs.pop("headers", {})

        if self.session:
            return self.session.request(method, url, headers=headers, **kwargs)
        return requests.request(method, url, headers=headers, **kwargs)

    def get(self, url: str, **kwargs) -> requests.Response:
        """
        Performs a GET request.

        Args:
            url (str): URL to request.

        Returns:
            requests.Response: Response object.
        """

        logger.debug("BaseHTTPClient: Sent a HTTP GET Request", url=url, kwargs=kwargs)
        return self.make_request("GET", url, **kwargs)
