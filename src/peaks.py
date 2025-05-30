"""
MODULO: peaks.py

El modulo gestiona la lectura y el procesamiento de un archivo de picos de unión de factores de transcripción.

Funciones:
    leer_archivo_picos(ruta_picos)
    extraer_secuencias(picos_data, genoma)
"""


def leer_archivo_picos(ruta_picos):
    """
    Lee el archivo de picos y devuelve una lista de diccionarios con TF_name, start y end.
    """
    picos = [] # Variable que guardara la lista de diccionarios 

    with open(ruta_picos, "r") as archivo:
        encabezado = True  # Identificacion del encabezado
        for linea in archivo:
            if encabezado: 
                encabezado = False
                continue

            if linea.strip(): #Verificacion si  archivo esta vacio
                columnas = linea.strip().split("\t")
                if len(columnas) >= 3: # Identificacion al menos de 3 columnas para trabajar
                    nombre_tf = columnas[2] 
                    inicio = int(float(columnas[3])) 
                    final = int(float(columnas[4]))
                    picos.append({
                        "TF": nombre_tf, 
                        "start": inicio, 
                        "end": final
                    })
                          
    if not picos:
        print(f"El archivo {ruta_picos} esta vacio.")
        return None
   
    return picos


def extraer_secuencias(picos_data, genoma):
    """
    Agrupa las secuencias extraídas por TF_name en un diccionario
    """
    secuencias_por_tf = {} # Diccionario donde se agruparan TF_name

    for pico in picos_data: # Iteracion soble la lista de diccionarios de picos 
        nombre_tf = pico["TF"]
        inicio = pico["start"]
        final = pico["end"]
        secuencia = genoma[inicio:final]

        if nombre_tf not in secuencias_por_tf: # Reconocimiento de los sitios de union
            secuencias_por_tf[nombre_tf] = []

        secuencias_por_tf[nombre_tf].append(secuencia)
    
    return secuencias_por_tf