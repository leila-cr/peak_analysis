
# Proyecto de Automatización para la Identificación de Sitios de Unión de Factores de Transcripción en E. coli en experimentos de ChIP-Seq

Fecha: [30/05/2025]
Participantes: [Leilani Cruz Ramírez]


## Resumen

Este proyecto tiene como objetivo automatizar el proceso de identificación del sitio exacto de unión de los reguladores transcripcionales para 144 factores de transcripción (TFs) en el genoma completo de *Escherichia coli*. Las regiones de unión de estos TFs se han determinado mediante la técnica ChIP-seq.

## Estructura del proyecto
```
peak_analysis/              # Directorio raíz del proyecto
│
├── data/                   # Datos de entrada
│   ├── E_coli_K12.txt             # Genoma de referencia en formato FASTA
│   └── union_peaks_file.tsv       # Archivo con las regiones de unión (picos) para los TFs
│
├── doc/                    # Documentación del proyecto
│   ├── detalles_proyecto.md       # Descripción técnica y contexto del proyecto
│   ├── README_TF_B...md           # README principal del proyecto
│   └── test_cases.md              # Casos de prueba documentados
│
├── results/                # Resultados del análisis (se generarán aquí)
│
├── src/                    # Código fuente
│   ├── extract_fasta.py           # Extrae secuencias FASTA a partir del archivo de picos
│   ├── genome.py                  # Módulo de manejo del genoma (carga y acceso)
│   ├── io_utils.py                # Funciones de entrada/salida y utilidades generales
│   ├── main.py                    # Script principal para ejecutar todo el flujo
│   └── peaks.py                   # Procesamiento de información sobre los picos
│
├── .gitignore              # Archivos/Directorios excluidos del control de versiones
```

## Datos Disponibles

### Archivo de Picos
Contiene información sobre las regiones de unión de los 144 factores de transcripción. Se organiza en las siguientes columnas:

- **Dataset_Ids**: Identificadores de los datasets. Cada identificador representa un experimento o condición específica bajo la cual se identificaron los sitios de unión para el TF correspondiente.
- **TF_name**: Nombre del factor de transcripción que se une a la secuencia de ADN especificada.
- **Peak_start**: Posición inicial del pico de unión en el genoma.
- **Peak_end**: Posición final del pico de unión en el genoma.
- **Peak_center**: Posición central del pico de unión en el genoma.
- **Peak_number**: Número secuencial del pico, útil para referencias internas dentro del mismo conjunto de datos.
- **Max_Fold_Enrichment**: Enriquecimiento máximo observado en el pico.
- **Max_Norm_Fold_Enrichment**: Enriquecimiento máximo normalizado.
- **Proximal_genes**: Genes próximos al sitio de unión.
- **Center_position_type**: Tipo de posición central del pico (por ejemplo, intergénica, intrónica, etc.).

### Genoma Completo de E. coli
Disponible en un archivo formato FASTA.
- Archivo FASTA: **E_coli_K12.txt** (originalmente E_coli_K12_MG1655_U00096.3.txt)


## Objetivos del Proyecto

### Generación de Archivos FASTA
Desarrollar un programa en lenguaje python que extraiga y compile las secuencias de picos para cada TF en archivos individuales en formato FASTA. Cada archivo  que se genera representará un regulador específico.

## Ejecución del Programa

### Dependencias necesarias:
-**Python 3.12**
-**Modulos  estándar implementados por python**

### Comando general:
```
python main.py --fasta ../data/E_coli_K12.txt --tsv ../data/union_peaks_file.tsv --resultados ../results
```

### Descripción de los argumentos :
```
--tsv: Ruta al archivo .tsv que contiene los picos de unión de los TFs.

--fasta: Archivo FASTA con el genoma de E. coli.

--resultados: Carpeta donde se guardarán los archivos FASTA individuales y resultados del análisi
```

## Colaboración y Recursos

El proyecto será colaborativo, trabajando conjuntamente con un investigador. Se compartirán los siguientes recursos con el colaborador:
- Secuencias en formato FASTA de todos los TFs.
- Archivo genoma de referencia `U00096.3.fna`.
- Script para la generación de archivos FASTA y la ejecución
- URL del repositorio de GitHub donde se aloja el proyecto y el código, facilitando el feedback y las contribuciones, seguimiento y revicion de todos los colaboradores.

## Buenas Prácticas de Desarrollo

Para asegurar la calidad y mantenibilidad del software, el proyecto seguirá estas buenas prácticas:

- **Control de Versiones**: Uso de Git para el control de versiones, asegurando una gestión eficaz de los cambios y la colaboración.
- **Revisión de Código**: Implementación de revisiones de código periódicas para mejorar la calidad del software y compartir conocimientos entre el equipo.
- **Documentación Exhaustiva**: Mantener una documentación completa tanto del código como de los procesos operativos, asegurando que cualquier nuevo colaborador pueda integrarse fácilmente.
- **Pruebas Automatizadas**: Desarrollo de pruebas automatizadas para validar la funcionalidad y robustez del software.

## Plan de Implementación

1. **Desarrollo del Extractor de Secuencias**: Programación de la tarea que consiste en genera los archivos FASTA a partir del archivo de picos. Como es un proceso automatizado, todos la información requerida para ejecutar los programas debe ser por línea de comandos.
2. **Automatización del Análisis con `meme`**: Scripting del proceso de ejecución del análisis de motivos para cada TF.
3. **Integración y Pruebas**: Combinación de los módulos desarrollados y realización de pruebas integrales para asegurar la funcionalidad.
4. **Despliegue y Capacitación**: Implementación del sistema en el servidor del colaborador y capacitación de usuarios sobre su uso.

## Licencia
El proyecto  está licenciado bajo la Licencia MIT.

## Contacto
<email:leilanic@lcg.unam.mx> 
