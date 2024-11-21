import pytest
from progarchivespy.common.entity import Entity, EntityEnum


class MockEntityEnum(EntityEnum):  # Renamed from TestEntityEnum
    ARTIST = Entity(id=1, name="Artist")
    ALBUM = Entity(id=2, name="Album")
    SONG = Entity(id=3, name="Song")


def test_build_with_id():
    """
    Test that build returns the correct entity using the id.
    """
    entity = MockEntityEnum.build(id=1)
    assert entity is not None
    assert entity == MockEntityEnum.ARTIST


def test_build_with_name():
    """
    Test that build returns the correct entity using the name.
    """
    entity = MockEntityEnum.build(name="Album")
    assert entity is not None
    assert entity == MockEntityEnum.ALBUM


def test_build_with_id_and_name():
    """
    Test that build returns the correct entity when both id and name are provided.
    """
    entity = MockEntityEnum.build(id=3, name="Song")
    assert entity is not None
    assert entity == MockEntityEnum.SONG


def test_build_with_no_match():
    """
    Test that build returns None when no match is found.
    """
    entity = MockEntityEnum.build(id=99)
    assert entity is None

    entity = MockEntityEnum.build(name="Unknown")
    assert entity is None


def test_build_with_missing_id_and_name():
    """
    Test that build raises a ValueError when neither id nor name are provided.
    """
    with pytest.raises(ValueError, match="Either id or name must be provided"):
        MockEntityEnum.build()


def test_entity_enum_id_property():
    """
    Test that the id property of the enum works correctly.
    """
    assert MockEntityEnum.ARTIST.id == 1
    assert MockEntityEnum.ALBUM.id == 2
    assert MockEntityEnum.SONG.id == 3


def test_entity_enum_name_property():
    """
    Test that the name property of the enum works correctly.
    """
    assert MockEntityEnum.ARTIST.name == "Artist"
    assert MockEntityEnum.ALBUM.name == "Album"
    assert MockEntityEnum.SONG.name == "Song"
