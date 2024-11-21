# parsers/breadcrumb_parser.py
from bs4.element import Tag
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Breadcrumb(ABC, Generic[T]):
    """
    Wraps a bs4 element and provides a method to parse it into a desired result type.

    Attributes:
        element (Tag): The bs4 element to be wrapped and parsed.
    """

    @property
    def element(self) -> Tag:
        return self.__element

    @element.setter
    def element(self, value: Tag):
        if not isinstance(value, Tag):
            raise ValueError(f"element must be a bs4 Tag, not a {type}")

        self.__element = value

    def __init__(self, element: Tag):
        self.element = element

    @abstractmethod
    def parse(self) -> T:
        """
        Parses the element into the desired result type.

        Returns:
            T: Parsed result.
        """
