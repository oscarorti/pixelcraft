import replicate
import validators

import error

from prompts import style


def generate(
    prompt: str, image: str = None, style_filter: style.StyleFilter = None
) -> str:
    model = "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b"

    if style_filter:
        prompt = _concatenate_prompt_with_style(
            base_prompt=prompt, style_filter=style_filter
        )
    input_ = {"prompt": prompt}

    if image:
        is_valid = validators.url(image)
        if not is_valid:
            raise error.NotValidURL()
        input_.update({"image": image})

    try:
        output = replicate.run(model, input=input_)
        url = output[0]
    except Exception as e:
        raise Exception(e) from e
    return url


def _concatenate_prompt_with_style(
    base_prompt: str, style_filter: style.StyleFilter
) -> str:
    if style_filter != style.StyleFilter.NONE:
        styled_prompt = f"{base_prompt}, {style_filter.value}."
    else:
        styled_prompt = base_prompt
    return styled_prompt
