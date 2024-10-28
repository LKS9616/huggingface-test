API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"

def get_headers(token):
    return {"Authorization": f"Bearer {token}"}