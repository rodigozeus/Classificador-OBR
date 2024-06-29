import cv2
import os

# Cria as pastas se não existirem
folders = ['a', 'w', 'd']
for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Abre a webcam (geralmente o índice 0 se refere à primeira webcam USB conectada)
cap = cv2.VideoCapture(0)

# Verifica se a webcam foi aberta corretamente
if not cap.isOpened():
    print("Erro ao abrir a webcam")
    exit()

# Inicializa contadores de imagens para cada pasta
counters = {folder: 0 for folder in folders}

while True:
    # Captura um frame da webcam
    ret, frame = cap.read()

    # Verifica se o frame foi capturado corretamente
    if not ret:
        print("Erro ao capturar o frame")
        break

    # Mostra o frame em uma janela
    cv2.imshow('Webcam', frame)

    # Verifica se uma tecla foi pressionada
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        # Se a tecla 'q' for pressionada, sai do loop
        break
    elif key == ord('a'):
        # Salva a imagem na pasta 'a'
        filename = f'a/{counters["a"]}.jpg'
        cv2.imwrite(filename, frame)
        counters['a'] += 1
        print(f'Imagem {filename} salva')
    elif key == ord('w'):
        # Salva a imagem na pasta 'w'
        filename = f'w/{counters["w"]}.jpg'
        cv2.imwrite(filename, frame)
        counters['w'] += 1
        print(f'Imagem {filename} salva')
    elif key == ord('d'):
        # Salva a imagem na pasta 'd'
        filename = f'd/{counters["d"]}.jpg'
        cv2.imwrite(filename, frame)
        counters['d'] += 1
        print(f'Imagem {filename} salva')

# Libera a webcam
cap.release()

# Fecha todas as janelas abertas
cv2.destroyAllWindows()


