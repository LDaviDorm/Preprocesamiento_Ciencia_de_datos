# Proyecto de Calidad de Datos Bibliográficos UNAM 2024–2025

Proyecto final de la materia **Preprocesamiento para Ciencia de Datos**.

## Tema

Integración, perfilado, limpieza y análisis de datos bibliográficos de la UNAM en **Ciencias de la Computación**, correspondientes al periodo **marzo de 2024 a diciembre de 2025**.

El dominio del proyecto no es médico. La estructura general del proyecto de la materia se adaptó al dominio bibliográfico/académico.

## Objetivo

Construir una base bibliográfica limpia, integrada, de-duplicada y curada, usando un modelo canónico común para publicaciones académicas de la UNAM en Ciencias de la Computación.

El resultado final es una base en formato artículo–autor, donde cada fila representa una relación entre un artículo y un autor UNAM.

## Fuentes bibliográficas

Se trabajaron ocho fuentes:

- ACM Digital Library
- EBSCO
- Engineering Village
- IEEE Xplore
- ProQuest
- ScienceDirect
- Scopus
- Web of Science

## Modelo canónico

La base final conserva las siguientes 14 columnas:

```text
indice
Titulo
Año
Autor_norm
Afiliacion1
Afiliacion2
ISBN
ISSN
Doi
URL
Area
Subarea
Keywords
Abstract
```

## Áreas válidas

```text
ISBD  Ingeniería de Software y Bases de Datos
CC    Computación Científica
IA    Inteligencia Artificial
TC    Teoría de la Computación
SIAV  Señales, Imágenes y Ambientes Virtuales
RS    Redes y Seguridad
```

## Resultado final

La base curada final se ubica en:

```text
05_Correcciones/UNAM_Completo_2024_2025.csv
```

Métricas finales reportadas:

- 905 filas artículo–autor
- 406 artículos únicos
- 550 autores únicos
- 14 columnas canónicas
- 0 filas sin autor
- 0 filas sin afiliación principal
- 0 áreas fuera de catálogo
- URL completa para todos los registros

## Estructura del repositorio

```text
00_control/
01_recoleccion_manual/
02_modelo canonico/
03_perfilado/
04_Limpieza/
05_Correcciones/
06_LLM/
visualizaciones/
notebooks/
src/
outputs/
docs/
```

## Flujo general

```text
recolección manual
→ modelo canónico
→ integración preliminar
→ perfilado
→ limpieza
→ normalización de autores y afiliaciones
→ de-duplicación y fusión
→ curaduría manual
→ base limpia final
→ SQLite + TF-IDF + grafos
→ consultas heterogéneas con LLM local
→ visualizaciones y conclusiones
```

## Componentes de análisis

La etapa de análisis utiliza:

- SQLite para consultas tabulares.
- TF-IDF para búsqueda textual y similitud temática.
- NetworkX para grafo principal y subgrafo de coautoría.
- Ollama con `qwen2.5:7b` como LLM local para redactar respuestas a partir de evidencia calculada.

## Nota sobre datos

Los archivos CSV/XLSX del proyecto pueden subirse al repositorio si su tamaño es manejable. Evitar subir archivos temporales, respaldos duplicados, `.ipynb_checkpoints`, ambientes virtuales o caches.
