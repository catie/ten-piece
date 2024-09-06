import pytest
from ten_piece.data.factory.tag import TagFactory
from tests.fixtures.tag import TEST_TAGS


@pytest.mark.parametrize("test_tag", TEST_TAGS)
def test_valid_tags(tag_factory: TagFactory, test_tag):
    tag = tag_factory.create_new(tag_string=test_tag)

    parts = tag_factory.split_tag_string(tag_string=test_tag)
    normalized = tag_factory.normalize_tag_parts(tag_parts=parts)
    tag_type, tag_subtype, tag_value = normalized

    normalized_string = tag_factory.build_tag_string(tag_parts=normalized)

    assert tag.tag_id == normalized_string
    assert tag.tag_type == tag_type
    assert tag.tag_subtype == tag_subtype
    assert tag.tag_value == tag_value
    assert tag.display_name == parts[2]
