import replicate


def generate(prompt: str) -> str:
    try:
        model = "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b"
        output = replicate.run(model, input={"prompt": prompt})
        url = output[0]
    except Exception as e:
        raise Exception(e) from e
    return url
