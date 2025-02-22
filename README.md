## Problema #1: Agente de Semáforo Inteligente (Reactivo)
-	**Descripción:**
-	El problema consiste en un agente inteligente que controle un semáforo, cambiando su estado (Verde, Amarillo y Rojo), estos cambiarán según el flujo del tráfico. El agente es capaz de ajustar su duración de cada estado, según los vehículos que se detecten.

-	**Funcionamiento**
-	El código trabaja por medio de hilos para poder detectar los vehículos o tráfico y tambien para poder manejar el cambio del estado del semáforo.
-	Otro hilo ajusta el tiempo en verde si se llega a detectar un aumento en el tráfico.
-	Por último, se muestra en pantalla el estado actual y el tiempo que se espera en cada cambio.

## Problema #2: Agente Buscador de Objetos (Basado en Objetivos)
-	**Descripción:**
-	Este problema requiere desarrollar un agente que se pueda desplazar en una cuadricula de (5x5) haciendo una búsqueda de un objeto colocado de forma aleatoria, este avanza paso a paso hasta lograr encontrarlo.

-	**Funcionamiento**
-	Se usa el algoritmo BFS para poder hacer una búsqueda ampliada, logrando encontrar un objeto puesto aleatoriamente.
-	Se muestra la cuadricula en cada avance que del agente.
-	Si el agente encuentra el objeto, se muestra un mensaje de éxito.

## Problema 3: Sistema Experto para Diagnóstico Simple
-	**Descripción:**
-	Este problema requiere realizar un diagnóstico básico según los síntomas que se ingresen por el usuario.

-	**Funcionamiento**
-	Se solicita al usuario ingresar síntomas
-	Se aplican reglas condicionales para verificar el diagnostico.
-	Se muestra el diagnóstico del usuario.
-	Diagnósticos posibles:
-	Posible Migraña, Posible lesión muscular, posible alergia, Posible presión arterial baja, Posible infección urinaria, Posible problema de columna, Posible condición pulmonar crónica y Posible infección de garganta.

## Problema 4: Agente de Recomendación de Películas (Basado en Aprendizaje)
-	**Descripción:**
-	Este problema requiere diseñar un agente que recomiende películas tomando en cuenta el género favorito del usuario.
-	**Funcionamiento**
-	Se carga un diccionario de películas organizadas por género
-	Solicitud al usuario para poder ingresar el género favorito.
-	Se muestra una recomendación aleatoria del género seleccionado.
-	Se muestran los géneros disponibles.
