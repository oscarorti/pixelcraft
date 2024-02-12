FROM python:3.10-slim

WORKDIR /pixelcraft
# Define an environment variable for the Replicate token, this will be overriden in execution time
ENV REPLICATE_API_TOKEN=""
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "generate_image.py", "--prompt"]
