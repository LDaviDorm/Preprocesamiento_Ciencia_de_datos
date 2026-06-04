# Instrucciones para reproducir el proyecto

Este documento explica cómo ejecutar el proyecto en una computadora distinta a la computadora original de desarrollo.

El objetivo es que una persona externa pueda clonar el repositorio, instalar las dependencias, abrir los notebooks y revisar o regenerar los resultados principales sin depender de rutas locales específicas.

---

## 1. Clonar el repositorio

Abrir una terminal y ejecutar:

```bash
git clone https://github.com/LDaviDorm/Preprocesamiento_Ciencia_de_datos.git
cd Preprocesamiento_Ciencia_de_datos
```

Después de clonar, la estructura general del repositorio debe conservarse, especialmente las carpetas:

```text
00_control/
01_recoleccion_manual/
02_modelo canonico/
03_perfilado/
04_Limpieza/
05_Correcciones/
06_LLM/
notebooks/
```

---

## 2. Crear un ambiente virtual

Se recomienda usar un ambiente virtual para instalar las dependencias del proyecto sin afectar otras instalaciones de Python.

### En Windows

Desde la raíz del repositorio:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install --upgrade pip
.\.venv\Scripts\python -m pip install -r requirements.txt
```

### En macOS o Linux

Desde la raíz del repositorio:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

---

## 3. Abrir Jupyter Notebook

### En Windows

```powershell
.\.venv\Scripts\python -m notebook
```

### En macOS o Linux

```bash
python -m notebook
```

Se recomienda abrir Jupyter desde la raíz del repositorio.
También es posible abrirlo desde la carpeta `notebooks`, ya que los notebooks detectan automáticamente la raíz del proyecto.

---

## 4. Rutas del proyecto

Los notebooks fueron ajustados para no depender de rutas locales como:

```text
C:\Users\...
```

ni de rutas temporales como:

```text
/mnt/data
```

Cada notebook detecta automáticamente la raíz del repositorio y construye las rutas con `pathlib.Path`.

Por ello, el proyecto puede ejecutarse en otra computadora siempre que se conserve la estructura del repositorio.

---

## 5. Orden sugerido de ejecución

Los notebooks se encuentran en la carpeta:

```text
notebooks/
```

El orden sugerido de ejecución es:

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

---

## 6. Archivos principales del proyecto

### Base final curada

```text
05_Correcciones/UNAM_Completo_2024_2025.csv
```

Esta es la base final artículo–autor.

### Archivos para grafos

```text
06_LLM/00_Grafos/BD_UNAM_Graph_LLM.gml
06_LLM/00_Grafos/BD_UNAM_Sub_Graph_LLM.gml
```

Estos archivos se generan con el notebook:

```text
05_crear_grafos_llm_principal.ipynb
```

### Archivos para SQLite y TF-IDF

```text
06_LLM/01_Datos/UNAM_Completo_2024_2025.sqlite
06_LLM/01_Datos/tfidf_articulos.joblib
06_LLM/01_Datos/tfidf_autores.joblib
```

Estos archivos se generan con el notebook:

```text
06_preparar_sqlite_tfidf_simple.ipynb
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

Estos archivos permiten revisar los resultados del LLM sin necesidad de volver a ejecutar el modelo local.

---

## 7. Uso del LLM local con Ollama

El notebook:

```text
07_responder_preguntas_llm_local.ipynb
```

usa un modelo de lenguaje local mediante Ollama.

El modelo no está incluido dentro del repositorio.
Para regenerar las respuestas del LLM en otra computadora, se debe instalar Ollama y descargar el modelo usado en el proyecto.

Modelo utilizado:

```text
qwen2.5:7b
```

Para descargarlo:

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

Sin embargo, las respuestas ya generadas se encuentran guardadas en:

```text
06_LLM/02_Consultas/
```

Por lo tanto, pueden revisarse sin ejecutar nuevamente el modelo local.

---

## 8. Reproducción sin regenerar el LLM

Si sólo se desea revisar el proyecto y sus resultados finales, no es obligatorio regenerar las respuestas del LLM.

En ese caso, basta con revisar los archivos ya generados:

```text
06_LLM/02_Consultas/respuestas_20_preguntas_llm_corregido.csv
06_LLM/02_Consultas/trazabilidad_20_preguntas_llm_corregido.csv
06_LLM/02_Consultas/respuestas_20_preguntas_llm_corregido.txt
06_LLM/02_Consultas/diagnostico_uso_llm_corregido.txt
```

Para volver a generar esos archivos desde cero, sí es necesario tener Ollama activo y el modelo `qwen2.5:7b` instalado.

---

## 9. Prueba mínima de reproducibilidad

Después de clonar el repositorio e instalar las dependencias, se recomienda hacer una prueba mínima.

Abrir Jupyter Notebook:

```powershell
.\.venv\Scripts\python -m notebook
```

Luego abrir y ejecutar las primeras celdas de configuración de estos notebooks:

```text
01_convertir_fuentes_a_modelo_canonico.ipynb
02_unir_integrado_preliminar.ipynb
03_perfilado_integrado_preliminar.ipynb
05_crear_grafos_llm_principal.ipynb
06_preparar_sqlite_tfidf_simple.ipynb
07_responder_preguntas_llm_local.ipynb
```

Cada notebook debe detectar automáticamente la raíz del repositorio.

Un ejemplo de salida válida sería:

```text
Raíz del proyecto: C:\...\Preprocesamiento_Ciencia_de_datos
```

La ruta puede cambiar según la computadora, pero no debe aparecer una ruta fija de la computadora original.

---

## 10. Prueba completa de reproducibilidad

Para probar el proyecto como lo haría una persona externa, se recomienda clonar el repositorio en una carpeta nueva.

Ejemplo:

```bash
git clone https://github.com/LDaviDorm/Preprocesamiento_Ciencia_de_datos.git prueba_reproducibilidad
cd prueba_reproducibilidad
```

Después instalar dependencias:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install --upgrade pip
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python -m notebook
```

Luego abrir los notebooks y verificar que:

* no busquen rutas locales de otra computadora;
* no usen rutas `/mnt/data`;
* encuentren los archivos requeridos dentro del repositorio;
* generen las salidas esperadas en las carpetas correspondientes.

---

## 11. Posibles errores y solución

### Error: no se encontró la raíz del proyecto

Posible causa:

* Jupyter se abrió desde una carpeta que no pertenece al repositorio.

Solución:

* Cerrar Jupyter.
* Abrir una terminal en la raíz del repositorio.
* Ejecutar nuevamente:

```powershell
.\.venv\Scripts\python -m notebook
```

---

### Error: falta un archivo requerido

Posible causa:

* No se ejecutó un notebook anterior.
* El archivo no está incluido en el repositorio.
* El archivo fue renombrado.

Solución:

* Revisar el orden de ejecución indicado en el `README.md`.
* Revisar que el archivo exista en la ruta indicada.
* Si el archivo se genera en una etapa anterior, ejecutar primero el notebook correspondiente.

---

### Error: falta una dependencia de Python

Posible causa:

* No se instaló correctamente `requirements.txt`.

Solución:

```powershell
.\.venv\Scripts\python -m pip install -r requirements.txt
```

Si el error menciona `tabulate`, instalarlo con:

```powershell
.\.venv\Scripts\python -m pip install tabulate
```

---

### Error: Ollama no responde

Posible causa:

* Ollama no está instalado.
* El servicio local de Ollama no está activo.
* El modelo `qwen2.5:7b` no está descargado.

Solución:

```bash
ollama pull qwen2.5:7b
ollama list
```

Si el servicio no está activo:

```bash
ollama serve
```

Después volver a ejecutar el notebook del LLM.

---

## 12. Nota sobre nombres de carpetas

Algunas carpetas deben conservar exactamente su nombre actual porque los notebooks dependen de esas rutas.

Por ejemplo, si la carpeta existe como:

```text
04_Limpieza/03_Nomralizar_Nombres
```

debe conservarse con ese mismo nombre, aunque tenga una falta de escritura, a menos que se modifiquen todos los notebooks que hacen referencia a ella.

---

## 13. Resultado esperado

Al finalizar el flujo, los archivos principales esperados son:

```text
05_Correcciones/UNAM_Completo_2024_2025.csv
06_LLM/00_Grafos/BD_UNAM_Graph_LLM.gml
06_LLM/00_Grafos/BD_UNAM_Sub_Graph_LLM.gml
06_LLM/01_Datos/UNAM_Completo_2024_2025.sqlite
06_LLM/01_Datos/tfidf_articulos.joblib
06_LLM/01_Datos/tfidf_autores.joblib
06_LLM/02_Consultas/respuestas_20_preguntas_llm_corregido.csv
06_LLM/02_Consultas/trazabilidad_20_preguntas_llm_corregido.csv
```

Estos archivos permiten revisar la base final, los grafos, los artefactos de búsqueda y las respuestas generadas por el LLM local.

---

## 14. Observación final

Este repositorio fue ajustado para ser ejecutado fuera de la computadora original de desarrollo.
La reproducibilidad depende de conservar la estructura de carpetas, instalar las dependencias indicadas y, si se desea regenerar el LLM, contar con Ollama y el modelo `qwen2.5:7b`.
