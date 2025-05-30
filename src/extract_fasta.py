import os
import argparse


def cargar_genoma(ruta_fasta):
    """
    Carga el genoma desde un archivo FASTA y devuelve una unica cadena de texto.
    """
    nucleotidos = "" # Variable para concatenar la secuencia de nucleotidos
    
    with open(ruta_fasta, "r") as archivo:
         es_fasta = False   
         for linea in archivo:  # Se itera sobre cada linea del archivo
            linea = linea.strip()
            if linea.startswith(">"):
                es_fasta = True # Validacion del archivo en formato FASTA
            elif es_fasta:
                nucleotidos += linea.upper() # Concatenacion de las lineas de secuencia

    if not es_fasta: 
        print(f"El archivo {ruta_fasta} no es compatible")
        return None
    
    return nucleotidos


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


def guardar_fasta_por_tf(secuencias_por_tf, ruta_salida):
    """
    Guarda archivos FASTA separados por cada TF_name
    """
    for nombre_tf in secuencias_por_tf: 
        ruta_archivo = ruta_salida + "/" + nombre_tf + ".fasta" # Creacion de los archivos FASTA por cada TF
        archivo = open(ruta_archivo, "w")

        for i, secuencia in enumerate(secuencias_por_tf[nombre_tf]):
            archivo.write(">peak_" + str(i+1) + "\n") # Estructura de la primera linea del archivo fasta '>'
            archivo.write(secuencia + "\n") # Se escribe la secuencia que corresponde al factor

        archivo.close()  

    print("Archivos FASTA guardados correctamente.")


def main():
    parser = argparse.ArgumentParser(description="Procesamiento de los archivos de entrada (FASTA y tsv)")
    parser.add_argument("--fasta", required=True, help="Ruta del archivo FASTA de entrada")
    parser.add_argument("--tsv", required= True, help="Ruta del archivo TSV de entrada")
    parser.add_argument("--resultados", required= True, help="Directorio donde se guardaran los archivos FASTA por cada TF")

    args = parser.parse_args()

    ruta_fasta = args.fasta
    ruta_picos = args.tsv
    ruta_salida = args.resultados

    if not os.path.exists(ruta_salida):
        os.makedirs(ruta_salida)

    genoma = cargar_genoma(ruta_fasta)
    if genoma is None:
        return
    
    picos_data =leer_archivo_picos(ruta_picos)
    if picos_data is None:
        return
    secuencias_por_tf = extraer_secuencias(picos_data, genoma)
    guardar_fasta_por_tf(secuencias_por_tf, ruta_salida)


if __name__ == "__main__":
    main()

