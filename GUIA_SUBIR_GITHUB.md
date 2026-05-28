# Guía rápida para subir a GitHub

Ejecuta estos comandos desde la carpeta raíz del proyecto.

## 1. Inicializar repositorio

```bash
git init
git add .
git commit -m "Version inicial del proyecto de calidad de datos bibliograficos UNAM"
```

## 2. Crear repositorio en GitHub

En GitHub crea un repositorio nuevo, por ejemplo:

```text
proyecto-calidad-datos-bibliograficos-unam
```

No agregues README desde GitHub si ya tienes este README local.

## 3. Conectar remoto

Cambia `USUARIO` por tu usuario de GitHub:

```bash
git remote add origin https://github.com/USUARIO/proyecto-calidad-datos-bibliograficos-unam.git
git branch -M main
git push -u origin main
```

## 4. Actualizaciones posteriores

```bash
git status
git add .
git commit -m "Actualiza limpieza, analisis y documento final"
git push
```

## 5. Si algún archivo es demasiado grande

GitHub limita archivos grandes. Si un archivo supera el límite, no lo subas directamente. Opciones:

- comprimirlo;
- usar Git LFS;
- dejarlo fuera y documentar su ubicación local;
- subir una muestra y mantener el archivo completo localmente.
