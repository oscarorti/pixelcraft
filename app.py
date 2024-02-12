import streamlit as st
from models import sdxl
from prompts import style

st.title("Pixelcraft")
prompt = st.text_input(
    label="Enter a prompt for the image generation:",
    value="An astronaut riding a rainbow unicorn",
)

image_url = st.text_input(
    label="Enter the URL of a reference image (optional):",
    value=None,
)

if image_url:
    st.image(image=image_url, caption="Reference image", use_column_width=True)

filter_option = st.selectbox(
    label="Select a style filter (optional):",
    options=[f.name for f in style.StyleFilter],
)

if st.button("Generate Image"):
    try:
        selected_filter = style.StyleFilter[filter_option]
        result_url = sdxl.generate(
            prompt=prompt, image=image_url, style_filter=selected_filter
        )
        st.image(image=result_url, caption="Generated Image")
        st.success("Image generated successfully!")
    except Exception as e:
        st.error(f"Failed to generate image: {e}")
