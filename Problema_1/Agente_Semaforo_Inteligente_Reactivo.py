import time
import random
from threading import Thread, Event

class AgenteSemaforo:
    def __init__(self):
        self.estado = "Rojo"  # Esta en Rojo del Semaforo
        self.tiempo_verde = 15  # Tiempo en verde (cuando inicia)
        self.tiempo_amarillo = 3  # Tiempo en amarillo (Intermedio)
        self.tiempo_rojo = 5  # Tiempo en rojo (Para y deteccion)
        self.evento_trafico = Event()  # Evento para poder simular los carros o trafico
        self.vehiculos_detectados = 0  # La cantidad de vehículos que se detecten

    def detectar_vehiculos(self):
        """Se inicia la simulación para detectar los vehículos"""
        while True:
            time.sleep(2)  # Dos segundos para dejar la simulación
            self.vehiculos_detectados = random.randint(0, 20)
            print(f"Vehículos detectados: {self.vehiculos_detectados}")
            if self.vehiculos_detectados > 15:
                self.evento_trafico.set()  # Se habilita el evento de trafico intenso
            else:
                self.evento_trafico.clear()  # Se desactiva el evento y sigue detectando

    def ajustar_tiempos(self):
        """Se hace el ajuste del tiempo dependiendo la cantidad de vehículos"""
        if self.vehiculos_detectados > 15:
            self.tiempo_verde = 20  # Si hay mucho tráfico, mas tiempo en verde
        elif self.vehiculos_detectados > 5:
            self.tiempo_verde = 15  # Se usa el tiempo normal en verde
        else:
            self.tiempo_verde = 8  # Si hay poco trafico, menos tiempo en verde

    def cambiar_estado(self):
        """Se cambia el estado del semáforo"""
        while True:
            if self.estado == "Verde":
                self.estado = "Amarillo"
                tiempo_espera = self.tiempo_amarillo
            elif self.estado == "Amarillo":
                self.estado = "Rojo"
                tiempo_espera = self.tiempo_rojo
            else:
                self.estado = "Verde"
                tiempo_espera = self.tiempo_verde

            print(f"El semáforo está en {self.estado} → tiempo: {tiempo_espera} segundos.")
            time.sleep(tiempo_espera)

            # Se ajusta el tiempo, si se activa el evento del trafico
            if self.evento_trafico.is_set():
                self.ajustar_tiempos()
                print("Ajustando de tiempo por trafico intenso")

    def ejecutar(self):
        """Acá se ejecuta el agente del semáforo"""
        # Este hilo detecta los vehículos
        hilo_deteccion = Thread(target=self.detectar_vehiculos)
        hilo_deteccion.daemon = True  # Si el programa termina el hilo se detiene
        hilo_deteccion.start()

        # Se cambia el estado del semáforo
        hilo_semaforo = Thread(target=self.cambiar_estado)
        hilo_semaforo.daemon = True
        hilo_semaforo.start()

        # While para mantener el programa en bucle
        while True:
            time.sleep(1)

# Creación y ejecución del agente
semaforo = AgenteSemaforo()
semaforo.ejecutar()