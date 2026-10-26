import os
from pathlib import Path
# Forma tradicional con el módulo os
os.replace('antiguo_nombre.txt', 'nuevo_nombre.txt')
# Forma orientada a objetos con pathlib
# origen = Path('antiguo_nombre.txt')
# origen.rename('nuevo_nombre.txt') # o origen.replace(...)