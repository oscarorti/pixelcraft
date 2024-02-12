import streamlit as st
from models import sdxl

st.title("Pixelcraft")
prompt = st.text_input(
    label="Enter a prompt for the image generation:",
    value="An astronaut riding a rainbow unicorn",
)
if st.button(label="Generate Image"):
    try:
        image_url = sdxl.generate(prompt=prompt)
        st.image(image=image_url, caption="Generated Image")
        st.success("Image generated successfully!")
    except Exception as e:
        st.error(f"Failed to generate image: {e}")
