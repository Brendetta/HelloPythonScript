from pathlib import Path
directorio = Path('.')
# Buscar todos los archivos de Python en la carpeta actual
for script in directorio.glob('*.py'):
    print(f"Fichero: {script.name} | Nombre base: {script.stem} | Extensión: {script.suffix}")