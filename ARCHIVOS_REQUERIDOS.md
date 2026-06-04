# Archivos requeridos del proyecto

Este documento lista los archivos principales usados por los notebooks.

## Base final

| Archivo | Descripción |
|---|---|
| `05_Correcciones/UNAM_Completo_2024_2025.csv` | Base final corregida del proyecto |

## Archivos para grafos

| Archivo | Descripción |
|---|---|
| `06_LLM/00_Grafos/BD_UNAM_Graph_LLM.gml` | Grafo principal usado para análisis |
| `06_LLM/00_Grafos/BD_UNAM_Sub_Graph_LLM.gml` | Subgrafo de coautoría |

## Archivos para SQLite y TF-IDF

| Archivo | Descripción |
|---|---|
| `06_LLM/01_Datos/UNAM_Completo_2024_2025.sqlite` | Base SQLite para consultas |
| `06_LLM/01_Datos/tfidf_articulos.joblib` | Artefacto TF-IDF de artículos |
| `06_LLM/01_Datos/tfidf_autores.joblib` | Artefacto TF-IDF de autores |

## Preguntas y respuestas LLM

| Archivo | Descripción |
|---|---|
| `06_LLM/02_Consultas/preguntas_consultas_heterogeneas_simple.csv` | Preguntas usadas para consultar el sistema |
| `06_LLM/02_Consultas/respuestas_20_preguntas_llm_corregido.csv` | Respuestas generadas por el LLM local |
| `06_LLM/02_Consultas/trazabilidad_20_preguntas_llm_corregido.csv` | Trazabilidad de las respuestas |
| `06_LLM/02_Consultas/respuestas_20_preguntas_llm_corregido.txt` | Respuestas en formato de lectura |
| `06_LLM/02_Consultas/diagnostico_uso_llm_corregido.json` | Diagnóstico de uso del LLM |
| `06_LLM/02_Consultas/diagnostico_uso_llm_corregido.txt` | Diagnóstico en formato de lectura |
