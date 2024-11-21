from progarchivespy.common.http import HTTPClient, BaseHTTPClient
from progarchivespy.services import TopAlbumsService


class ProgArchivesClient:
    """
    Client class for interacting with ProgArchives API.

    Provides direct access to the various service layers of this library.

    Attributes:
        top_albums (TopAlbumsService): Service for interacting with the top albums endpoint.
    """

    def __init__(self, http_client: HTTPClient | None = None):
        """
        Initialize the ProgArchives client.

        Args:
            http_client (HTTPClient, optional): A Requests-like HTTP client. Defaults to None.
        """
        http_client = http_client or BaseHTTPClient()

        self.top_albums = TopAlbumsService(http_client)
