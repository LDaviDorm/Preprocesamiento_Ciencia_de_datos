"""
Validación rápida de la estructura del repositorio y de la base final.

Uso:
    python src/validar_repositorio.py
"""

from pathlib import Path
import pandas as pd

CANONICAL_COLUMNS = [
    "indice", "Titulo", "Año", "Autor_norm", "Afiliacion1", "Afiliacion2",
    "ISBN", "ISSN", "Doi", "URL", "Area", "Subarea", "Keywords", "Abstract"
]

VALID_AREAS = {"ISBD", "CC", "IA", "TC", "SIAV", "RS"}

REQUIRED_DIRS = [
    "00_control",
    "01_recoleccion_manual",
    "02_modelo canonico",
    "03_perfilado",
    "04_Limpieza",
    "05_Correcciones",
    "06_LLM",
    "visualizaciones",
    "notebooks",
    "src",
    "outputs",
    "docs",
]

def main():
    root = Path.cwd()
    print("Validando repositorio en:", root)

    print("\n[1] Carpetas principales")
    for d in REQUIRED_DIRS:
        path = root / d
        print(f" - {d}: {'OK' if path.exists() else 'FALTA'}")

    print("\n[2] Base final")
    final_csv = root / "05_Correcciones" / "UNAM_Completo_2024_2025.csv"
    if not final_csv.exists():
        print(" - FALTA:", final_csv)
        return

    df = pd.read_csv(final_csv, dtype=str, encoding="utf-8-sig").fillna("")
    print(" - Archivo:", final_csv)
    print(" - Filas:", len(df))
    print(" - Columnas:", len(df.columns))

    cols_ok = list(df.columns) == CANONICAL_COLUMNS
    print(" - Columnas canónicas exactas:", "OK" if cols_ok else "REVISAR")
    if not cols_ok:
        print("   Columnas encontradas:", list(df.columns))

    print(" - Artículos únicos:", df["indice"].nunique() if "indice" in df else "N/A")
    print(" - Autores únicos:", df["Autor_norm"].nunique() if "Autor_norm" in df else "N/A")

    if "Autor_norm" in df:
        print(" - Filas sin autor:", (df["Autor_norm"].str.strip() == "").sum())
    if "Afiliacion1" in df:
        print(" - Filas sin Afiliacion1:", (df["Afiliacion1"].str.strip() == "").sum())
    if "Area" in df:
        bad_areas = sorted(set(df["Area"].str.strip()) - VALID_AREAS - {""})
        print(" - Áreas fuera de catálogo:", bad_areas if bad_areas else "OK")

    print("\nValidación terminada.")

if __name__ == "__main__":
    main()
