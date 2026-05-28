# Estructura del repositorio

Esta estructura respeta la organización final usada en la computadora local del proyecto.

## 00_control

Archivos base y referencias:

- `ModeloCanonico.xlsx`
- `ControldeDatos.xlsx`
- `UNAM_Completo_Corregido.xlsx`
- notas de la tutora
- archivos de referencia

## 01_recoleccion_manual

Evidencia de la búsqueda manual.

```text
01_recoleccion_manual/
├── 00_bitacora_general/
├── 01_queries/
├── 02_reportes_busqueda/
└── 03_descargas_raw/
```

## 02_modelo canonico

Archivos convertidos al modelo canónico y unión preliminar.

```text
02_modelo canonico/
├── 01_por_fuente/
├── 02_por_area/
├── 03_union/
└── 00_reportes/
```

## 03_perfilado

Reportes de perfilado del integrado preliminar.

## 04_Limpieza

Fases de limpieza.

```text
04_Limpieza/
├── 00_Separacion_Autor_Afiliacion/
├── 01_Normalizar_Afiliaciones/
├── 02_Normalizar_Columnas/
├── 03_Nomralizar_Nombres/
└── 04_deduplicar/
```

Nota: se conserva `03_Nomralizar_Nombres` para coincidir con la ruta local usada durante el proyecto.

## 05_Correcciones

Curaduría manual y base final.

Archivo principal:

```text
05_Correcciones/UNAM_Completo_2024_2025.csv
```

## 06_LLM

Recursos para consultas heterogéneas con LLM.

```text
06_LLM/
├── 00_Grafos/
├── 01_SQLite_TFIDF/
├── 02_Preguntas/
└── 03_Consultas/
```

## visualizaciones

Gráficas generadas para el PDF.

## notebooks

Libretas ejecutables del proyecto.

## src

Funciones reutilizables.

## outputs

Reportes, logs y tablas generadas.

## docs

Documentación final, secciones LaTeX y PDF.
