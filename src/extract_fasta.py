#Cargar el archivo FASTA del genoma
def cargar_genoma(fasta_path):
    """Carga el genoma desde un archivo FASTA y devuelve una única cadena de texto."""
    genome = "" #Variable donde se va a concatenar toda la secuencia de nucleotidos
   
    with open(fasta_path, "r") as infile:
         file_is_fasta = False   
         for line in infile:  #Se itera sobre cada linea del archivo
            line = line.strip()
            if line.startswith(">"):
                file_is_fasta = True #Validacion del archivo en formato FASTA
            elif file_is_fasta:
                genome += line.upper() #Se van concatenando las lineas para obtener la cadena

    if not file_is_fasta: #En caso que no se encontro '>'
        print(f"El archivo {fasta_path} no es compatible")
        return None
    
    #print(f"Cantidad de bases:{len(genome)} en el genoma.") VERIFICANDO CANTIDAD DE NUCLEOTIDOS
    return genome


#Cargar archivo picos de union
def leer_archivo_picos(peaks_path): 
    """Lee el archivo de picos y devuelve una lista de diccionarios con TF_name, start y end."""
    peaks = [] #Lista para guardar la informacion de los picos
   

    with open(peaks_path, "r") as infile:
        first_line = True #Para identificar el encabezado
        for line in infile:
            if first_line:#No tomar en cuenta la linea del encabezado
                first_line = False
                continue

            if line.strip():#Verificar si el archivo esta vacio, si se genera una lista vacia
                column = line.strip().split("\t")

                if len(column) >= 3:#Para poder obtener la info se necesita al menos las 3 columnas que buscamos
                    tf_name = column[2] 
                    start = int(float(column[3])) #Se pasan a valores numericos para poder trabajar con ellos
                    end = int(float(column[4]))
                    peaks.append({"TF": tf_name, "start": start, "end": end})#Se guarda diccionarios en la lista vacia 
                          
    if not peaks:#Si el archivo despues de leerse sigue vacio
        print(f"El archivo {peaks_path} esta vacio.")
        return None
    #print(f"Se han cargado {len(peaks)} picos correctamente.")

    return peaks


def extraer_secuencias(peaks_data, genoma):
    """Agrupa las secuencias extraídas por TF_name en un diccionario."""
    tf_sequences = {} #Diccionario donde se agruparan TF_name

    for peak in peaks_data: #Se itera soble la lista de diccionarios de picos registrados
        tf_name = peak["TF"]
        start = peak["start"]
        end = peak["end"]
        sequence = genoma[start:end]

        if tf_name not in tf_sequences: #Reconocimiento de los sitios de union, filtrando los demas nucleotidos
            tf_sequences[tf_name] = []

        tf_sequences[tf_name].append(sequence)
    
    return tf_sequences

def guardar_fasta_por_tf(sequence_for_tf, output_dir):
    """Guarda archivos FASTA separados por cada TF_name."""

    for tf_name in sequence_for_tf:#IteraR sobre cada factor esta en el diccionario
        file_path = output_dir + "/" + tf_name + ".fasta"#Creacion de los archivos FASTA
        outfile = open(file_path, "w")

        for i, sequence in enumerate(sequence_for_tf[tf_name]):
            outfile.write(">peak_" + str(i+1) + "\n")#Se escribe la primera linea del archivo fasta '>'
            outfile.write(sequence + "\n")#Se escribe la secuencia que corresponde al factor

        outfile.close()  # Cerrar archivo después de escribir

    print("FASTA guardados.")


#Llamado a las funciones
fasta_path = "./../data/E_coli_K12_MG1655_U00096.3.txt"
genoma = cargar_genoma(fasta_path)
        

peaks_path = "./../data/union_peaks_file.tsv"
peaks_data = leer_archivo_picos(peaks_path)


output_dir = "./../results/fasta_por_tf"
sequence_for_tf = extraer_secuencias(peaks_data, genoma)
#print(f"Se extrajeron secuencias para {len(sequence_for_tf)} factores de transcripción.")



