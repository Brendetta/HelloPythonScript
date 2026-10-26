import shutil
from pathlib import Path
import time
# Metadatos de un fichero
archivo = Path("datos.txt")
if archivo.exists():
    stats = archivo.stat()
    print(f"Tamaño: {stats.st_size} bytes")
    print(f"Última modificación: {time.ctime(stats.st_mtime)}")
# Espacio en disco (Multiplataforma)
    total, usado, libre = shutil.disk_usage("respaldos")
    print(f"Espacio libre en disco: {libre // (1024**3)} GB")