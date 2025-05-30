"""
MODULO: main.py

Este es el punto de entrada del programa
"""
import os
import argparse

from genome import cargar_genoma
from peaks import leer_archivo_picos, extraer_secuencias
from io_utils import guardar_fasta_por_tf


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