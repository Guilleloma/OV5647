from picamera2 import Picamera2
from time import sleep

def prueba_camara():
    try:
        # Inicializamos la cámara
        picam2 = Picamera2()

        # Configuración básica
        picam2.configure(picam2.create_still_configuration())

        # Iniciamos la cámara
        print("Iniciando previsualización...")
        picam2.start()

        # Guardamos una imagen de prueba
        sleep(5)  # Dejamos la cámara encendida por 5 segundos para capturar correctamente
        print("Capturando imagen...")
        archivo_imagen = "/home/pi/robot/camera/captura_prueba.jpg"
        picam2.capture_file(archivo_imagen)

        print(f"Imagen capturada y guardada en '{archivo_imagen}'.")

        # Detenemos la cámara
        picam2.stop()

    except Exception as e:
        print(f"Error al usar la cámara: {e}")

if __name__ == "__main__":
    prueba_camara()
