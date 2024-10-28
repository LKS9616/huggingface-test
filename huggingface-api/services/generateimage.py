import requests
import io
from PIL import Image

def generate_image(api_url, headers, text):
    response = requests.post(api_url, headers=headers, json={"inputs": text})
    image = Image.open(io.BytesIO(response.content))
    return image