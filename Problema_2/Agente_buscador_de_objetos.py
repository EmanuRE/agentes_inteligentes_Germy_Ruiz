import random

class AgenteBuscador:
    def __init__(self):
        self.filas = 5
        self.columnas = 5
        self.cuadricula = [[None for _ in range(self.columnas)] for _ in range(self.filas)]
        self.agente_fila, self.agente_columna = 0, 0  # Primer posición del Agente
        self.objeto_fila, self.objeto_columna = self.colocar_objeto()  # Establece la posicion del objeto

    def colocar_objeto(self):
        """Se coloca el objeto en un punto aleatorio de la cuadricula"""
        # Logica para poner el objeto
        pass

    def mostrar_cuadricula(self):
        """Se muestra la cuadricula y la posicion del agente con el objeto"""
        # Implementar la logica para la cuadricula
        pass

    def mover_agente(self):
        """Se usa el camino encontrado y se mueve el agente hacia el objeto"""
        # La logica para mover el agente
        pass

    def ejecutar(self):
        """Se ejecuta el agente para buscar"""
        # La logica para ejecutar el agente
        pass

# Creación y Ejecución del agente
agente = AgenteBuscador()
agente.ejecutar()