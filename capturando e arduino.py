import cv2
import os
import serial
import time

# Configuração da porta serial
ser = serial.Serial('/dev/ttyAMA0', 9600)  # Usando a porta GPIO - Pinos TX (GPI14, pino 8) - RX (GPI15, pino 10)
time.sleep(2)

# Função para ver quantos arquivos tem e continuar dai
def contar_arquivos(pasta):
    files = [f for f in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, f))]
    if not files:
        return 0
    numbers = [int(os.path.splitext(f)[0]) for f in files if f.split('.')[0].isdigit()]
    return max(numbers) + 1 if numbers else 0

# Cria as pastas se não existirem e inicializa contadores de imagens para cada pasta
pastas = ['a', 'w', 'd']
counters = {}
for pasta in pastas:
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    counters[pasta] = contar_arquivos(pasta)

# Abre a webcam
cap = cv2.VideoCapture(0)

while True:
    # Captura um frame da webcam
    ret, frame = cap.read()

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
        ser.write(b'a')  # Envia 'a' para o Arduino
    elif key == ord('w'):
        # Salva a imagem na pasta 'w'
        filename = f'w/{counters["w"]}.jpg'
        cv2.imwrite(filename, frame)
        counters['w'] += 1
        print(f'Imagem {filename} salva')
        ser.write(b'w')  # Envia 'w' para o Arduino
    elif key == ord('d'):
        # Salva a imagem na pasta 'd'
        filename = f'd/{counters["d"]}.jpg'
        cv2.imwrite(filename, frame)
        counters['d'] += 1
        print(f'Imagem {filename} salva')
        ser.write(b'd')  # Envia 'd' para o Arduino

# Libera a webcam
cap.release()

# Fecha todas as janelas abertas
cv2.destroyAllWindows()

# Fecha a comunicação serial
ser.close()
