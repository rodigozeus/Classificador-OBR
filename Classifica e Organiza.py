import os
import cv2
import numpy as np
import shutil
from tensorflow.keras.models import load_model

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (160, 120))
    image = image / 255.0
    return image

# modelo
model = load_model('/home/rodigozeus/Downloads/Teste/modelo_direcao.keras')

# imagens
input_directory = '/home/rodigozeus/Downloads/Teste/fotos'

# destino
output_directories = {
    0: '/home/rodigozeus/Downloads/Teste/fotos/direita',
    1: '/home/rodigozeus/Downloads/Teste/fotos/esquerda',
    2: '/home/rodigozeus/Downloads/Teste/fotos/frente'
}

for dir in output_directories.values():
    os.makedirs(dir, exist_ok=True)
    
    
def get_unique_filename(directory, filename):
    base, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(directory, new_filename)):
        new_filename = f"{base}_{counter}{extension}"
        counter += 1
    return new_filename

for image_name in os.listdir(input_directory):
    if image_name.endswith('.jpg'):
        image_path = os.path.join(input_directory, image_name)
        print(image_path)
        image = preprocess_image(image_path)
        image = np.expand_dims(image, axis=0)

        prediction = model.predict(image, verbose=0)
        
        class_index = np.argmax(prediction)

        output_directory = output_directories[class_index]
        unique_filename = get_unique_filename(output_directory, image_name)
        output_path = os.path.join(output_directory, unique_filename)

        shutil.move(image_path, output_path)
        print(f"Imagem {image_name} movida para {output_directory} como {unique_filename}")
            
            
