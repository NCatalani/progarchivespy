from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from progarchivespy.common.http import HTTPClient

T = TypeVar("T")


class Service(ABC, Generic[T]):
    def __init__(self, http_client: HTTPClient):
        self.http_client = http_client

    @abstractmethod
    def parse_response(self, raw_response: str) -> T: ...

    @abstractmethod
    def query(self, *args, **kwargs) -> T: ...
