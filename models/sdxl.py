import replicate
import validators

import error


def generate(prompt: str, image: str = None) -> str:
    model = "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b"
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
