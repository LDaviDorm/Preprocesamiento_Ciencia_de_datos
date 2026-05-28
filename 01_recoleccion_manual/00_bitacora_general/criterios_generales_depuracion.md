# Criterios generales de depuración preliminar

Este documento resume las reglas comunes usadas durante la recolección manual y depuración preliminar de artículos bibliográficos de la UNAM en Ciencias de la Computación.

## 1. Periodo válido

Se aceptan registros correspondientes al periodo:

```text
Marzo de 2024 a diciembre de 2025
```

Reglas aplicadas:

- No se aceptan registros de 2026.
- No se aceptan registros anteriores a marzo de 2024 cuando el mes es verificable.
- Si una fuente sólo reporta año 2024 sin mes verificable, el registro puede conservarse para revisión posterior.
- Si existen varias fechas, se prioriza la fecha bibliográfica o del evento/publicación sobre fechas de indexación, cuando así lo indique el reporte de la editorial.

## 2. Afiliación UNAM

Se aceptan registros con afiliación institucional clara a la Universidad Nacional Autónoma de México.

Variantes consideradas:

- Universidad Nacional Autónoma de México
- Universidad Nacional Autonoma de Mexico
- National Autonomous University of Mexico
- UNAM
- U.N.A.M.
- IIMAS-UNAM
- variantes con acentos, sin acentos, mayúsculas y minúsculas

Reglas de rechazo:

- No se acepta un registro sólo porque mencione a la UNAM como caso de estudio, corpus, dataset o institución analizada.
- No se acepta `UNAM` cuando corresponde a otra institución distinta de la Universidad Nacional Autónoma de México.
- Si la afiliación no es clara, el registro se descarta o se deja como pendiente de revisión.

## 3. Pertenencia a Ciencias de la Computación

Se acepta un registro si el aporte principal es computacional.

Ejemplos de aportes aceptables:

- método, algoritmo o arquitectura computacional;
- software, framework, pipeline o herramienta computacional;
- sistema de información, base de datos o recuperación de información;
- modelo computacional generalizable;
- procesamiento de texto, imágenes, señales o datos;
- seguridad, criptografía, redes o protocolos;
- HCI, interfaces, realidad virtual/aumentada o interacción;
- cómputo científico, HPC, GPU, simulación computacional, métodos numéricos;
- IA, ML, NLP, visión, robótica, GNN, LLM, RAG u optimización cuando el aporte es metodológico o técnico.

Reglas de rechazo:

- No se acepta un artículo sólo porque use software, una base de datos, un algoritmo, IA, machine learning, simulación, imágenes, señales, red, sensor, plataforma, Python, toolbox o análisis de datos como herramienta secundaria.
- No se aceptan artículos cuyo aporte principal sea de medicina, biología, química, materiales, geociencias, energía, astronomía, educación, ciencias sociales u otra disciplina sin contribución computacional generalizable.

## 4. Deduplicación preliminar

En esta fase la deduplicación fue interna por lote o área.

Criterios:

1. DOI exacto.
2. Si no hay DOI: título normalizado + año + primer autor.
3. Cuando hay versiones duplicadas, conservar el registro con mayor completitud de metadatos.
4. La deduplicación global entre áreas y editoriales queda pendiente.

## 5. Área y subárea

La columna o carpeta de área usada durante la búsqueda representa el área inicial del lote.

Todavía queda pendiente:

- clasificación final de área;
- asignación final de subárea;
- resolución de registros recuperados en un área pero pertenecientes a otra.

## 6. Modelo canónico

El modelo canónico final del proyecto será:

```text
indice, Titulo, Año, Autor_norm, Afiliacion1, Afiliacion2, ISBN, ISSN, Doi, URL, Area, Subarea, Keywords, Abstract
```

En esta fase sólo ACM y ScienceDirect quedaron en modelo canónico o canónico parcial. Las demás fuentes conservan columnas originales y deben pasar por schema matching y schema mapping.

## 7. Estado de la fase

Esta fase se considera **recolección manual y depuración preliminar**, no integración final.
