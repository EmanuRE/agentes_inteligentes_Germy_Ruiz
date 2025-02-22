import random

def cargar_peliculas():
    """Diccionario de peliculas organizadas por genero"""
    peliculas = { 
    "acción": ["Die Hard", "The Raid", "Terminator 2: Judgment Day", "Skyfall", "Logan"],
    "comedia": ["Aterriza como Puedas", "Un Príncipe en Nueva York", "Zoolander", "Ted", "¿Qué Pasó Ayer?"],
    "drama": ["Cadena Perpetua", "La Lista de Schindler", "El Pianista", "Réquiem por un Sueño", "Una Mente Brillante"],
    "ciencia ficción": ["Ex Machina", "Dune", "Minority Report", "El Quinto Elemento", "Gattaca"],
    "terror": ["Un Lugar en Silencio", "La Bruja", "Midsommar", "El Babadook", "Actividad Paranormal"],
    }
    return peliculas ##Se almacenan las peliculas en un array

def solicitar_genero():
    """Se le pide al usuariio ingresar un genero favorito"""
    print("Estos géneros están disponibles: acción, comedia, drama, ciencia ficción, terror")
    genero = input("Ingresa tu género favorito: ").strip().lower()
    return genero

def recomendar_pelicula(peliculas, genero):
    """Se recomienda una pelicula segun el genero, de forma aleatoria"""
    if genero in peliculas:
        pelicula = random.choice(peliculas[genero])
        return f"Esta pelicula te recomendamos: {pelicula}"
    else:
        return "Este genero no es válida, elige una del listado."

def ejecutar_agente_recomendacion():
    """Ejecución del agente para recomendar una pelicula"""
    peliculas = cargar_peliculas()
    genero = solicitar_genero()
    recomendacion = recomendar_pelicula(peliculas, genero)
    print(recomendacion)

# Se ejecuta el agente de recomendación
ejecutar_agente_recomendacion()