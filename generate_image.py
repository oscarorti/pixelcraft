import argparse

from models import sdxl

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate images using AI with a given prompt. Use the --prompt argument followed by your desired text to generate an image."
    )
    parser.add_argument(
        "-p",
        "--prompt",
        type=str,
        required=True,
        help="Prompt for generating the image. Example usage: --prompt 'An astronaut riding a rainbow unicorn'",
    )
    parser.add_argument(
        "-i",
        "--image",
        type=str,
        required=False,
        default=None,
        help="Reference image for generating the image. Example usage: --image 'https://replicate.delivery/pbxt/O8vvaeb5GJ3wYacIM7SnUcB6Uj48GEc9jcGN65KJAeHWF6VSA/out-0.png'",
    )
    args = parser.parse_args()

    url = sdxl.generate(args.prompt, args.image)
    print(url)
