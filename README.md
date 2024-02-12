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
3. Create an account on [Replicate](https://replicate.com) and get the access token from your personal settings.

In [Replicate](https://replicate.com) there is a free tier, so you don't need to add billing information for demo purposes.

## Execution

### CLI
First of all, it is necessary to export the API token as environment variable:
```bash
export REPLICATE_API_TOKEN=<your_token_here>
```

Generate custom images from a prompt with:
```bash
python generate_image.py --prompt "An astronaut riding a rainbow unicorn"
```
Explore various prompts to discover the project's versatility.

Generate custom images from a prompt and a reference image with:
```bash
python generate_image.py \
  --prompt "An astronaut riding a rainbow cat" \
  --image "https://pbxt.replicate.delivery/YXbcLudoHBIYHV6L0HbcTx5iRzLFMwygLr3vhGpZI35caXbE/out-0.png"
```

Generate custom images from a prompt, a reference image, and a style filter with:
```bash
python generate_image.py \
  --prompt "Monna Lisa" \
  --image "https://media.npr.org/assets/img/2012/02/02/mona-lisa_custom-31a0453b88a2ebcb12c652bce5a1e9c35730a132-s1100-c50.jpg" \
  --filter "CARTOON"
```

For usage details:
```bash
python generate_image.py --help
```

### Streamlit App

This project includes a Streamlit app for an interactive image generation experience.

To run the Streamlit app, navigate to the project directory and execute the following command:

```bash
streamlit run app.py
```

#### With Docker

##### Build the Docker Image

To build the Docker image for running the script, navigate to the project directory and run:

```bash
docker build -t pixelcraft:latest .
```

##### Run with Docker

After building the Docker image, you can run the script inside a Docker container and pass a prompt directly using the `docker run` command.

For example:

```bash
docker run -p 8501:8501 -e REPLICATE_API_TOKEN=<your_api_token_here> pixelcraft:latest
```

## Development

### Pre-commit Hooks

Ensure code quality by setting up pre-commit hooks:

1. Install pre-commit: `pip install pre-commit`.
1. Run `pre-commit install` to activate hooks.

### Testing

Run unit tests to ensure reliability:

```bash
export PYTHONPATH=`pwd`
pytest tests/unit
```

## Prompt Engineering

### SDXL (StableDiffusionXL)

#### Resources
- [The Ultimate Guide to Write Great Prompts for Stable Diffusion](https://docs.kanaries.net/articles/stable-diffusion-prompt-guide)
- [Prompt Guide for Stable Diffusion XL (SDXL 1.0)](https://blog.segmind.com/prompt-guide-for-stable-diffusion-xl-crafting-textual-descriptions-for-image-generation/)
- [106 styles for Stable Diffusion XL model](https://stable-diffusion-art.com/sdxl-styles/)

## Future work

### Enhancing Content Consistency in AI-Generated Images

The following strategies, ordered by increasing complexity, could help to improve the content consistency when using the Stable Diffusion XL model:

1. **Detailed Prompt Engineering for the Style Filters**: Refining prompt construction to include more specific details and employing advanced techniques
can help to produce more precise outputs. The inclusion of vivid descriptions, emotional tones, and contextual specifics helps anchor the AI's creative
process, reducing ambiguity and enhancing consistency.

1. **Model Parameters Optimization**: Adjusting the configuration options available allows for a nuanced control over the generative process.
Fine-tuning these parameters can influence the creativity-consistency balance, enabling the generation of images that are both innovative and
aligned with user expectations.

1. **Use of ControlNet to Condition the Image Generation Process**: Incorporating ControlNet, or similar conditioning mechanisms, into the image generation
process enables the imposition of structural constraints on the output. By defining specific regions, shapes, or layouts, ControlNet guides the
generation process to predetermined compositional frameworks enhancing the consistency on the generated images.

1. **Human Feedback Loop**: Establishing an iterative refinement cycle, where initial outputs are analyzed and then used to improve the application.
This process of continuous feedback and modification allows for the fine-tuning of both the prompt and model parameters, optimizing the output for consistency and relevance.

1. **Custom Model Fine-tuning Using an Image Database from the Previous Step**: Custom fine-tuning of the Stable Diffusion XL model with a curated dataset.
This high quality dataset, derived from previous iterations of image generation and human validations, will help to produce better images with improved
content consistency results.

### Simplify user experience

Making the prompt optional and generating it from the input image will improve the user's experience and increase its adoption.

### Allow to upload a file from the local machine

Incorporating AWS S3 alongside with presigned URLs (or similar strategies in other cloud providers) for storing and utilizing local files instead of relying on public image URLs.

### Integration with more providers and own infrastructure

Adding integrations with MidJourney, Google Imagen, or an API in a private cloud with a custom model deployed would help to diversify the range of visual
content generation capabilities available to users. This strategic expansion enables the leveraging of distinct strengths and stylistic details that each
platform offers, and enriching the creative possibilities and output variety.

## Contributing

Contributions are welcome! Please submit issues and pull requests via GitHub. Follow our coding standards and include tests with your PRs.

## License

This project is licensed under [MIT License](LICENSE.txt) - see the license file for details.

## Contact

For support or inquiries, please open an issue in the project's GitHub issue tracker.
