"""
MODULO: io_utils.py

Contiene funciones estandar en python para guardar archivos FASTA generados a partir de secuencias  por factor de transcripción.

Funciones:
    guardar_fasta_por_tf(secuencias_por_tf, ruta_salida)
"""
import os

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