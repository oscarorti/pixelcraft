import argparse

from models import sdxl
from prompts import style

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
    parser.add_argument(
        "-f",
        "--filter",
        type=str,
        required=False,
        default=None,
        choices=[f.name for f in style.StyleFilter],
        help="Choose a style filter for the image. This option requires and input image.",
    )
    args = parser.parse_args()

    if args.filter:
        chosen_filter = style.StyleFilter[args.filter]
        if not args.image:
            raise ValueError("Image required if filter is selected")
    else:
        chosen_filter = None

    url = sdxl.generate(args.prompt, args.image, chosen_filter)

    print(url)
