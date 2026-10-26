from pathlib import Path
import json
def procesar_archivo_configuracion(ruta: str) -> None:
    archivo_path = Path(ruta)
    try:
        with archivo_path.open("r", encoding="utf-8") as f:
            contenido = json.load(f)
            print("Configuración cargada correctamente:", contenido)
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta}' no fue encontrado.")
    except PermissionError:
        print(f"Error: No tienes permisos de lectura sobre '{ruta}'.")
    except json.JSONDecodeError as e:
        print(f"Error: El archivo contiene un JSON mal formado en la línea {e.lineno}.")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Prueba de ejecución
procesar_archivo_configuracion("config_inexistente.json")