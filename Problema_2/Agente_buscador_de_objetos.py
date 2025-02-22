import random
from collections import deque
import time

class AgenteBuscadorBFS:
    def __init__(self):
        self.filas = 5
        self.columnas = 5
        self.cuadricula = [[None for _ in range(self.columnas)] for _ in range(self.filas)]
        self.agente_fila, self.agente_columna = 0, 0  # Primer posición del Agente
        self.objeto_fila, self.objeto_columna = self.colocar_objeto()  # Establece la posicion del objeto

    def colocar_objeto(self):
        """Se coloca el objeto en un punto aleatorio de la cuadricula"""
        fila = random.randint(0, self.filas - 1)
        columna = random.randint(0, self.columnas - 1) #Se usa random para un punto aleatorio
        return fila, columna

    def mostrar_cuadricula(self):
        """Se muestra la cuadricula y la posicion del agente con el objeto"""
        for fila in range(self.filas):
            for columna in range(self.columnas):
                if fila == self.agente_fila and columna == self.agente_columna:
                    print("A", end=" ")  # Asi se muestra al agente
                elif fila == self.objeto_fila and columna == self.objeto_columna:
                    print("♪", end=" ")  # Asi se representa al Objeto
                else:
                    print("-", end=" ")  # Simula la cuadricula 5x5
            print()  # Se muestra una linea despues de cada fila
        print()  # Separa cada movimiento

    def es_valido(self, fila, columna):
        """Se verifica si la posicion es correcta en la cuadricula"""
        return 0 <= fila < self.filas and 0 <= columna < self.columnas

    def encontrar_camino(self):
        """Se usa BFS para encontrar un camino corto"""
        cola = deque()
        cola.append((self.agente_fila, self.agente_columna, []))  # (BFS, busca fila, columna y establece el camino)
        visitado = set()

        while cola:
            fila, columna, camino = cola.popleft()

            if (fila, columna) == (self.objeto_fila, self.objeto_columna):
                return camino + [(fila, columna)]  # Se establece el camino completo

            if (fila, columna) in visitado:
                continue
            visitado.add((fila, columna))

            # Aca se definen los movimientos, arriba, abajo o lados
            movimientos = [(fila - 1, columna), (fila + 1, columna),
                           (fila, columna - 1), (fila, columna + 1)]

            for nueva_fila, nueva_columna in movimientos:
                if self.es_valido(nueva_fila, nueva_columna):
                    cola.append((nueva_fila, nueva_columna, camino + [(fila, columna)]))

        return None  # Posibilidad de no encontrar un camino

    def mover_agente(self):
        """Se usa el camino encontrado y se mueve el agente hacia el objeto"""
        camino = self.encontrar_camino()
        if not camino:
            print("No se pudo encontrar un camino hacia el objeto")
            return

        for paso in camino:
            self.agente_fila, self.agente_columna = paso
            self.mostrar_cuadricula()
            time.sleep(1)  # Tiempo de espera entre cada avance

        print("¡Se econtro el Objeto!")

    def ejecutar(self):
        """Se ejecuta el agente para buscar"""
        print("Posicion del Agente (A) y Objeto (♪): ")
        self.mostrar_cuadricula()
        self.mover_agente()

# Creación y Ejecución del agente
agente = AgenteBuscadorBFS()
agente.ejecutar()