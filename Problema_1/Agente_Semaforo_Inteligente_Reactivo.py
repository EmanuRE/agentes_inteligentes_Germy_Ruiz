import time
import random
from threading import Thread, Event

class AgenteSemaforo:
    def __init__(self):
        self.estado = "Rojo"  # Esta en Rojo del Semaforo
        self.tiempo_verde = 10  # Tiempo en verde (cuando inicia)
        self.tiempo_amarillo = 3  # Tiempo en amarillo (Intermedio)
        self.tiempo_rojo = 5  # Tiempo en rojo (Para y deteccion)
        self.evento_trafico = Event()  # Evento para poder simular los carros o trafico
        self.vehiculos_detectados = 0  # La cantidad de vehículos que se detecten

    def detectar_vehiculos(self):
        """Se inicia la simulación para detectar los vehículos"""
        #Logica para la deteccion de autos
        pass

    def ajustar_tiempos(self):
        """Se hace el ajuste del tiempo dependiendo la cantidad de vehículos"""
        # Logica para los tiempos.
        pass

    def cambiar_estado(self):
        """Se cambia el estado del semáforo"""
        # Logica para el cambio de estado del semaforo
        pass

    def ejecutar(self):
        """Acá se ejecuta el agente del semáforo"""
        # Logica para que funcione el agente
        pass

# Creación y ejecución del agente
semaforo = AgenteSemaforo()
semaforo.ejecutar()