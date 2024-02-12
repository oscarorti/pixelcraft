import streamlit as st
from models import sdxl

st.title("Pixelcraft")
prompt = st.text_input(
    label="Enter a prompt for the image generation:",
    value="An astronaut riding a rainbow unicorn",
)

image_url = st.text_input(
    label="Enter the URL of a reference image (optional):",
    value=None,
)

if image_url is not None:
    st.image(image=image_url, caption="Reference image", use_column_width=True)

if st.button("Generate Image"):
    try:
        if image_url:
            result_url = sdxl.generate(prompt=prompt, image=image_url)
        else:
            result_url = sdxl.generate(prompt=prompt)

        st.image(image=result_url, caption="Generated Image")
        st.success("Image generated successfully!")
    except Exception as e:
        st.error(f"Failed to generate image: {e}")
