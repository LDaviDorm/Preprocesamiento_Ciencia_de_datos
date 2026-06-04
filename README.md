# Proyecto de Calidad de Datos Bibliográficos UNAM 2024–2025

Proyecto final de la materia **Preprocesamiento para Ciencia de Datos**.

## Tema

Integración, perfilado, limpieza y análisis de datos bibliográficos de la UNAM en **Ciencias de la Computación**, correspondientes al periodo **marzo de 2024 a diciembre de 2025**.

## Objetivo

Construir una base bibliográfica limpia, integrada, de-duplicada y curada, usando un modelo canónico común para publicaciones académicas de la UNAM en Ciencias de la Computación.

El resultado final es una base en formato artículo–autor, donde cada fila representa una relación entre un artículo y un autor UNAM.

## Fuentes bibliográficas

Se trabajaron ocho fuentes:

* ACM Digital Library
* EBSCO
* Engineering Village
* IEEE Xplore
* ProQuest
* ScienceDirect
* Scopus
* Web of Science

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

* 905 filas artículo–autor
* 406 artículos únicos
* 550 autores únicos
* 14 columnas canónicas
* 0 filas sin autor
* 0 filas sin afiliación principal
* 0 áreas fuera de catálogo
* URL completa para todos los registros

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
docs/
```

## Flujo general del proyecto

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

* SQLite para consultas tabulares.
* TF-IDF para búsqueda textual y similitud temática.
* NetworkX para grafo principal y subgrafo de coautoría.
* Ollama con `qwen2.5:7b` como LLM local para redactar respuestas a partir de evidencia calculada.

## Reproducibilidad

Los notebooks fueron ajustados para no depender de rutas locales de una computadora específica, como:

```text
C:\Users\...
```

ni de rutas temporales como:

```text
/mnt/data
```

Cada notebook detecta automáticamente la raíz del repositorio y construye las rutas usando `pathlib.Path`.

Por ello, el proyecto puede ejecutarse desde otra computadora siempre que se conserve la estructura del repositorio y existan los archivos requeridos.

## Requisitos

Para ejecutar este proyecto se requiere:

* Python 3.10 o superior
* Git
* Jupyter Notebook
* Las dependencias listadas en `requirements.txt`
* Ollama sólo si se desea regenerar las respuestas del LLM local

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/LDaviDorm/Preprocesamiento_Ciencia_de_datos.git
cd Preprocesamiento_Ciencia_de_datos
```

Crear un ambiente virtual en Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install --upgrade pip
.\.venv\Scripts\python -m pip install -r requirements.txt
```

Abrir Jupyter Notebook:

```powershell
.\.venv\Scripts\python -m notebook
```

En macOS o Linux, se puede crear el ambiente con:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m notebook
```

## Orden sugerido de ejecución

Los notebooks se encuentran en la carpeta:

```text
notebooks/
```

Se recomienda ejecutarlos desde la raíz del repositorio o desde la carpeta `notebooks`.

El orden sugerido es:

```text
01_convertir_fuentes_a_modelo_canonico.ipynb
02_unir_integrado_preliminar.ipynb
03_perfilado_integrado_preliminar.ipynb
04_limpieza_00_separacion_autor_afiliacion_reglas_explicitas.ipynb
04_limpieza_01_catalogo_afiliaciones_unam_campus.ipynb
04_limpieza_02_catalogo_diccionario_afiliaciones_unam_final.ipynb
04_limpieza_03_normalizar_filtrar_afiliaciones_unam.ipynb
04_limpieza_04_normalizar_columnas_pre_deduplicacion_v2.ipynb
04_limpieza_05_corregir_observaciones_pre_deduplicacion.ipynb
04_limpieza_06_crear_diccionario_autores_unam.ipynb
04_limpieza_07_normalizar_nombres_autores.ipynb
04_limpieza_08_deduplicar_fusionar_pares.ipynb
05_crear_grafos_llm_principal.ipynb
06_preparar_sqlite_tfidf_simple.ipynb
07_responder_preguntas_llm_local.ipynb
```

## Archivos principales

### Base final

```text
05_Correcciones/UNAM_Completo_2024_2025.csv
```

### Archivos para grafos

```text
06_LLM/00_Grafos/BD_UNAM_Graph_LLM.gml
06_LLM/00_Grafos/BD_UNAM_Sub_Graph_LLM.gml
```

### Archivos para SQLite y TF-IDF

```text
06_LLM/01_Datos/UNAM_Completo_2024_2025.sqlite
06_LLM/01_Datos/tfidf_articulos.joblib
06_LLM/01_Datos/tfidf_autores.joblib
```

### Preguntas y respuestas del LLM

```text
06_LLM/02_Consultas/preguntas_consultas_heterogeneas_simple.csv
06_LLM/02_Consultas/respuestas_20_preguntas_llm_corregido.csv
06_LLM/02_Consultas/trazabilidad_20_preguntas_llm_corregido.csv
06_LLM/02_Consultas/respuestas_20_preguntas_llm_corregido.txt
06_LLM/02_Consultas/diagnostico_uso_llm_corregido.json
06_LLM/02_Consultas/diagnostico_uso_llm_corregido.txt
```

Los nombres anteriores deben coincidir con los archivos existentes dentro del repositorio. Si algún archivo fue renombrado, debe actualizarse también en los notebooks correspondientes.

## Uso del LLM local con Ollama

El notebook:

```text
07_responder_preguntas_llm_local.ipynb
```

utiliza un modelo de lenguaje local mediante Ollama.

El modelo no está incluido dentro del repositorio. Para regenerar las respuestas del LLM en otra computadora, se debe instalar Ollama y descargar el modelo usado en el proyecto:

```bash
ollama pull qwen2.5:7b
```

Para verificar que el modelo está instalado:

```bash
ollama list
```

Debe aparecer:

```text
qwen2.5:7b
```

El notebook se conecta al servicio local de Ollama mediante:

```text
http://localhost:11434
```

Si Ollama no está instalado, el servicio local no está activo o el modelo `qwen2.5:7b` no fue descargado, el notebook del LLM no podrá regenerar las respuestas.

Sin embargo, las respuestas finales ya generadas se encuentran guardadas en:

```text
06_LLM/02_Consultas/
```

Por lo tanto, pueden revisarse sin necesidad de ejecutar nuevamente el modelo local.

## Notas sobre rutas y nombres de carpetas

Algunos nombres de carpetas deben conservarse exactamente como aparecen en el repositorio porque los notebooks dependen de ellos.

Por ejemplo, si existe una carpeta llamada:

```text
04_Limpieza/03_Nomralizar_Nombres
```

debe mantenerse con ese mismo nombre, aunque contenga una falta de escritura, a menos que también se modifiquen todos los notebooks que hacen referencia a esa ruta.

## Validación de ejecución

Para comprobar que el repositorio es reproducible en otra computadora, se recomienda hacer una prueba en una carpeta nueva:

```bash
git clone https://github.com/LDaviDorm/Preprocesamiento_Ciencia_de_datos.git prueba_reproducibilidad
cd prueba_reproducibilidad
```

Después, instalar dependencias:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install --upgrade pip
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python -m notebook
```

La prueba mínima consiste en abrir los notebooks principales y verificar que detecten automáticamente la raíz del repositorio sin depender de una ruta local.

## Resultados esperados

Al finalizar el flujo, los principales resultados del proyecto son:

```text
05_Correcciones/UNAM_Completo_2024_2025.csv
06_LLM/00_Grafos/
06_LLM/01_Datos/
06_LLM/02_Consultas/
```

Estos archivos contienen la base final curada, los grafos, los artefactos de consulta y las respuestas generadas por el LLM local.

## Autor

Luis David Aguilar Colorado
Proyecto final de la materia **Preprocesamiento para Ciencia de Datos**.
