from __future__ import annotations
from enum import Enum
from typing import NamedTuple, TypeVar, Type

T = TypeVar("T", bound="EntityEnum")


class Entity(NamedTuple):
    """
    Base class for ProgArchives API entities.
    """

    id: int
    name: str


class EntityEnum(Enum):
    """
    Enum class for holding ProgArchives API entities.
    """

    @classmethod
    def build(cls: Type[T], id: int | None = None, name: str | None = None) -> T | None:
        """
        Given either an id or a name, returns the corresponding entity.

        Args:
            cls (Type[T]): The entity class.
            id (int, optional): Defaults to None.
            name (str, optional): Defaults to None.

        Raises:
            ValueError: Neither id nor name were provided.

        Returns:
            T | None: The entity if found, None otherwise.
        """
        if not id and not name:
            raise ValueError("Either id or name must be provided")

        for entity in cls:
            id_matches = id and entity.value.id == id
            name_matches = name and entity.value.name == name

            if id_matches or name_matches:
                return entity
        return None

    @property
    def id(self) -> int:
        return self.value.id

    @property
    def name(self) -> str:
        return self.value.name
