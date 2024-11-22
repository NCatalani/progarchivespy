from dataclasses import dataclass, asdict
from progarchivespy.common import EntityEnum


def custom_dict_factory(data):
    """
    Custom dict factory for asdict.
    Converts Enums to their value during serialization.
    """
    result = {}
    for key, value in data:
        if isinstance(value, EntityEnum):
            result[key] = value.value._asdict()  # Serialize Enum as its value
            continue

        result[key] = value
    return result


@dataclass
class Serializable:
    """
    Base class for serializable dataclasses.

    Provides a property to convert the dataclass to a dictionary.
    """

    @property
    def asdict(self) -> dict:
        return asdict(self, dict_factory=custom_dict_factory)
