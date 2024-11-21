class ProgArchivesPyException(Exception):
    """Base exception for ProgArchivesPy package."""

    pass


class ParseException(ProgArchivesPyException):
    """Exception raised when parsing fails."""

    pass
