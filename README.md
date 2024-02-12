# Pixelcraft

Pixelcraft is an AI-based image generation project that leverages advanced AI models to transform textual prompts into unique visual art. This project showcases the power of AI in creative processes, offering users the ability to generate a wide array of images from simple descriptions and reference images.

## Prerequisites

- Python 3.10 or higher

## Setup

1. Clone the repository with `git clone https://github.com/oscarorti/pixelcraft.git`.
2. Install required Python packages:
```bash
pip install -r requirements.txt
```

## Execution

### CLI

Generate custom images with:
```bash
python generate_image.py --prompt "An astronaut riding a rainbow unicorn"
```
Explore various prompts to discover the project's versatility.

For usage details:
```bash
python generate_image.py --help
```

## Development

### Pre-commit Hooks

Ensure code quality by setting up pre-commit hooks:

1. Install pre-commit: `pip install pre-commit`.
1. Run `pre-commit install` to activate hooks.

### Testing

Run unit tests to ensure reliability:

```bash
pytest tests/unit
```

## Contributing

Contributions are welcome! Please submit issues and pull requests via GitHub. Follow our coding standards and include tests with your PRs.

## License

This project is licensed under [MIT License](LICENSE.txt) - see the license file for details.

## Contact

For support or inquiries, please open an issue in the project's GitHub issue tracker.
