from models.translation import load_translation
from services.translation import translate
from services.generateimage import generate_image
from routers.router import process_and_display, save_image

model, tokenizer = load_translation()

API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": f"Bearer {token}"}

korean_text = "바다 위의 버스, 버스 안에서 바라보는 시점"

translated_text = translate(model, tokenizer, korean_text)
print(f"Translated text: {translated_text}")

image = generate_image(API_URL, headers, translated_text)

process_and_display(image)

save_image(image)