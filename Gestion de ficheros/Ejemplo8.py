import json
# 1. Objeto de datos inicial
configuracion = {
"aplicacion": "Sistema de Control",
"version": 1.2,
"usuarios_activos": ["Ana", "Íñigo", "María"],
"parametros": {"modo_oscuro": True, "reintentos": 3}
}
# 2. Guardar en disco (Serialización)
with open("config.json", "w", encoding="utf-8") as f:
    json.dump(configuracion, f, indent=4, ensure_ascii=False)
# 3. Leer desde disco, modificar y guardar (Deserialización)
try:
    with open("config.json", "r", encoding="utf-8") as f:
        datos = json.load(f)
    # Modificación en memoria (añadir un usuario)
        datos["usuarios_activos"].append("Carlos")
# Reescritura
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
        print("Archivo JSON actualizado con éxito.")
except json.JSONDecodeError as error:
    print(f"Error de sintaxis en la estructura del JSON: {error}")