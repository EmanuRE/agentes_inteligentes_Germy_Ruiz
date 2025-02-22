def solicitar_sintomas():
    """Se solicita al usuario ingresar su sintomas"""
    print("Ingresa los síntomas que tienes (separados por comas, por favor):")
    sintomas = input().strip().lower().split(",")
    return [s.strip() for s in sintomas]

def diagnosticar(sintomas):
    """Se realiza un diagnóstico basado en los sintomas"""
    if "dolor de cabeza" in sintomas and "náuseas" in sintomas and "vómitos" in sintomas:
        return "Se considera una posible migraña o intoxicación alimentaria."
    elif "dolor en las articulaciones" in sintomas and "hinchazón" in sintomas:
        return "Se considera una posible artritis o lesión muscular."
    elif "picazón en la piel" in sintomas and "erupciones" in sintomas:
        return "Posible alergia"
    elif "mareos" in sintomas and "visión borrosa" in sintomas:
        return "Posible presión arterial baja"
    elif "dolor al orinar" in sintomas and "fiebre" in sintomas:
        return "Se considera una posible infección urinaria."
    elif "dolor de espalda" in sintomas and "entumecimiento" in sintomas:
        return "Se considera un posible problema de columna vertebral."
    elif "tos persistente" in sintomas and "pérdida de peso" in sintomas:
        return "Se considera ser un signo de una condición pulmonar crónica."
    elif "dificultad para tragar" in sintomas and "dolor de garganta" in sintomas:
        return "Se considera una posible infección de garganta."
    else:
        return "Los síntomas no coinciden con ninguna condición de este sistema. Consulta a tu médico"

def ejecutar_sistema_experto():
    """Se ejecuta el sistema para el diagnóstico"""
    print("Sistema Experto (Diagnostico Simple)")
    sintomas = solicitar_sintomas()
    diagnostico = diagnosticar(sintomas)
    print("\nEste es tu diagnóstico:")
    print(diagnostico)

# Se ejecuta el sistema
ejecutar_sistema_experto()