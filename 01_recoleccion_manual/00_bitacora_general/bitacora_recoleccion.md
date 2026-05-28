# Bitácora general de recolección manual

## Proyecto

**Integración, perfilado, limpieza y análisis de datos bibliográficos de la UNAM en Ciencias de la Computación**

## Objetivo de esta fase

La fase de recolección manual tuvo como objetivo recuperar publicaciones académicas de la UNAM en Ciencias de la Computación, correspondientes al periodo **marzo de 2024 a diciembre de 2025**, a partir de fuentes bibliográficas heterogéneas.

Las fuentes trabajadas fueron:

1. ACM Digital Library
2. EBSCO Academic Search Ultimate
3. Engineering Village
4. IEEE Xplore
5. ProQuest Central
6. ScienceDirect
7. Scopus
8. Web of Science Core Collection

La búsqueda se organizó por editorial y por las seis áreas de la maestría:

- ISBD: Ingeniería de Software y Bases de Datos
- CC: Computación Científica
- IA: Inteligencia Artificial
- RS: Redes y Seguridad en Cómputo
- TC: Teoría de la Computación
- SIAV: Señales, Imágenes y Ambientes Virtuales

## Alcance de la fase

Esta fase comprende:

- documentación de queries por editorial y área;
- búsqueda manual en bases bibliográficas;
- descarga de archivos por lote;
- depuración preliminar para conservar registros de Ciencias de la Computación;
- identificación de falsos positivos;
- generación de reportes finales por editorial;
- organización de archivos por fuente.

## Qué NO se realizó todavía

Esta fase todavía **no** corresponde al integrado final. Quedan pendientes:

- conversión al modelo canónico de las fuentes que conservan columnas originales;
- correspondencia de esquemas formal por editorial;
- mapeo de esquemas al modelo canónico;
- perfilado global del integrado;
- limpieza global;
- deduplicación global entre editoriales;
- fusión de registros equivalentes;
- obtención del registro de oro;
- construcción del componente de grafo;
- construcción del componente textual/vectorial;
- consultas heterogéneas y visualizaciones finales.

## Criterio general de aceptación

Un registro se conservó de forma preliminar si cumplía con estos criterios:

1. pertenecer al periodo marzo 2024–diciembre 2025;
2. tener afiliación UNAM clara o una variante institucional inequívoca;
3. pertenecer claramente a Ciencias de la Computación;
4. tener metadatos suficientes para justificar su inclusión;
5. no ser únicamente un uso instrumental de software, base de datos, algoritmo, modelo, IA o simulación en otra disciplina.

## Observación sobre las fuentes

No todas las editoriales exportaron la información en el mismo formato. Algunas fuentes conservaron esquemas originales de exportación, mientras que ACM y ScienceDirect requirieron procesos especiales de extracción hacia el modelo canónico.

Por ello, esta etapa se considera una **depuración preliminar de fuentes heterogéneas**, no una integración final.
