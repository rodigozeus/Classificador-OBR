import cv2
import os

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (224, 224))  # Redimensionar para 224x224
    image = image / 255.0  # Normalizar para o intervalo [0, 1]
    return image

images = []
labels = []
for label in ["direita", "esquerda", "frente"]:
    for image_path in os.listdir(f"data/{label}"):
        image = preprocess_image(f"data/{label}/{image_path}")
        images.append(image)
        labels.append(label)
