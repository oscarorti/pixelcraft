import pytest
from unittest.mock import patch
from models import sdxl
import error


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


def test_generate_with_image():
    prompt = "Test prompt"
    image_url = "http://example.com/fake-image.png"
    expected_url = "http://example.com/fake-image-url"
    assert sdxl.generate(prompt, image=image_url) == expected_url


def test_replicate_run_called_with_correct_input_without_image(mock_replicate_run):
    prompt = "Test prompt without image"
    sdxl.generate(prompt)

    mock_replicate_run.assert_called_once_with(
        "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
        input={"prompt": prompt},
    )


def test_replicate_run_called_with_correct_input_with_image(mock_replicate_run):
    prompt = "Test prompt with image"
    image_url = "http://example.com/fake-image.png"
    sdxl.generate(prompt, image=image_url)

    mock_replicate_run.assert_called_once_with(
        "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
        input={"prompt": prompt, "image": image_url},
    )


def test_generate_with_invalid_image_url_raises_NotValidURL_error():
    prompt = "Test prompt"
    invalid_image_url = "not a valid url"
    with pytest.raises(error.NotValidURL):
        sdxl.generate(prompt, image=invalid_image_url)
