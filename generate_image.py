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
    args = parser.parse_args()

    url = sdxl.generate(args.prompt)
    print(url)
