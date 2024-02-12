import pytest
from unittest.mock import patch
from models import sdxl


@pytest.fixture(autouse=True)
def mock_replicate_run():
    with patch(
        "replicate.run", return_value=["http://example.com/fake-image-url"]
    ) as mock:
        yield mock


def test_generate_success():
    prompt = "Test prompt"
    expected_url = "http://example.com/fake-image-url"
    assert (
        sdxl.generate(prompt) == expected_url
    ), "The URL returned by the generate function should match the expected URL"


def test_generate_exception():
    with patch("replicate.run", side_effect=Exception("Test exception")):
        prompt = "Test prompt"
        with pytest.raises(Exception, match="Test exception"):
            sdxl.generate(prompt)
