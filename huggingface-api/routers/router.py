from IPython.display import display

def process_and_display(image):
    display(image)
    
def save_image(image, path="generated_image.png"):
    image.save(path)