import pytest
from unittest.mock import patch
from models import sdxl
from prompts import style
import error
import replicate


@pytest.fixture(autouse=True)
def mock_replicate_run():
    with patch(
        "replicate.run", return_value=["http://example.com/fake-image-url"]
    ) as mock:
        yield mock


def test_generate_with_prompt():
    prompt = "Test prompt"
    expected_url = "http://example.com/fake-image-url"
    assert (
        sdxl.generate(prompt) == expected_url
    ), "The URL returned by the generate function should match the expected URL"


def test_generate_raises_ImageGenerationError_on_replicate_run_ValueError():
    with patch("replicate.run", side_effect=ValueError("Test exception")):
        prompt = "Test prompt"
        with pytest.raises(error.ImageGenerationError, match="Test exception"):
            sdxl.generate(prompt)


def test_generate_raises_ImageGenerationError_on_replicate_run_ModelError():
    with patch(
        "replicate.run", side_effect=replicate.exceptions.ModelError("Test exception")
    ):
        prompt = "Test prompt"
        with pytest.raises(error.ImageGenerationError, match="Test exception"):
            sdxl.generate(prompt)


def test_generate_with_prompt_and_image():
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


def test_generate_with_prompt_and_style_filter(mock_replicate_run):
    prompt = "Test prompt"
    style_filter = style.StyleFilter.VINTAGE
    expected_prompt = f"{prompt}, {style_filter.value}."

    sdxl.generate(prompt, style_filter=style_filter)

    mock_replicate_run.assert_called_once_with(
        "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
        input={"prompt": expected_prompt},
    )


def test_generate_with_prompt_style_filter_and_image(mock_replicate_run):
    prompt = "Test prompt"
    image_url = "http://example.com/fake-image.png"
    style_filter = style.StyleFilter.CARTOON
    expected_prompt = f"{prompt}, {style_filter.value}."

    sdxl.generate(prompt, image=image_url, style_filter=style_filter)

    mock_replicate_run.assert_called_once_with(
        "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
        input={"prompt": expected_prompt, "image": image_url},
    )
