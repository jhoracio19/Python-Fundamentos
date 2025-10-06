import json
import os

RUTA_ARCHIVO = 'tareas.json'

def cargar_tareas():
    if not os.path.exists(RUTA_ARCHIVO):
        return []
    with open(RUTA_ARCHIVO, 'r') as f:
        return json.load(f)

def guardar_tareas(tarea):
    tareas = cargar_tareas()
    tareas.append(tarea)
    with open(RUTA_ARCHIVO, 'w') as f:
        json.dump(tareas, f, indent=4)

def actualizar_tareas(tareas):
    with open(RUTA_ARCHIVO, 'w', encoding='utf-8') as f:
        json.dump(tareas, f, indent=4, ensure_ascii=False)
