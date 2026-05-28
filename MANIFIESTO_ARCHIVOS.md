# Manifiesto de archivos principales esperados

Este manifiesto indica los archivos más importantes que deben existir antes de entregar.

## Base final

```text
05_Correcciones/UNAM_Completo_2024_2025.csv
```

## Reportes clave

```text
01_recoleccion_manual/00_bitacora_general/matriz_recoleccion.csv
02_modelo canonico/00_reportes/reporte_final_modelo_canonico_area_clasificada.txt
02_modelo canonico/03_union/resumen_integrado_preliminar.md
03_perfilado/resumen_perfilado_global.md
04_Limpieza/00_Separacion_Autor_Afiliacion/reporte_limpieza_separacion_articulo_autor.txt
04_Limpieza/01_Normalizar_Afiliaciones/reporte_limpieza_normalizacion_afiliaciones_unam.txt
04_Limpieza/02_Normalizar_Columnas/reporte_limpieza_normalizacion_columnas_pre_autor.txt
04_Limpieza/03_Nomralizar_Nombres/reporte_limpieza_normalizacion_nombres_autores.txt
04_Limpieza/04_deduplicar/reporte_limpieza_deduplicacion_fusion.txt
05_Correcciones/reporte_curaduria_manual_base_unam_2024_2025.txt
06_LLM/00_Grafos/reporte_generacion_grafos_llm.txt
06_LLM/01_SQLite_TFIDF/reporte_preparacion_sqlite_tfidf_simple.txt
06_LLM/03_Consultas/reporte_final_consultas_heterogeneas_llm.txt
06_LLM/03_Consultas/respuestas_20_preguntas_llm_corregido.txt
```

## Archivos de análisis

```text
06_LLM/00_Grafos/BD_UNAM_Graph_LLM.gml
06_LLM/00_Grafos/BD_UNAM_Sub_Graph_LLM.gml
06_LLM/00_Grafos/resumen_grafos_LLM.json
06_LLM/01_SQLite_TFIDF/UNAM_Completo_2024_2025.sqlite
06_LLM/01_SQLite_TFIDF/tfidf_articulos.joblib
06_LLM/01_SQLite_TFIDF/tfidf_autores.joblib
```

## Visualizaciones principales

```text
visualizaciones/grafos/01_distribucion_tipos_nodos_LLM.png
visualizaciones/grafos/02_top_autores_grado_coautoria_LLM.png
visualizaciones/grafos/BD_UNAM_Graph_LLM_vista_muestra.png
visualizaciones/grafos/BD_UNAM_Sub_Graph_LLM_vista_muestra.png
```
