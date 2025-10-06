import json
import os

RUTA_ARCHIVO = "usuarios.json"

def cargar_usuarios():
    if not os.path.exists(RUTA_ARCHIVO):
        return []
    with open(RUTA_ARCHIVO, "r") as f:
        return json.load(f)

def guardar_usuario(usuario):
    usuarios = cargar_usuarios()
    usuarios.append(usuario)
    with open(RUTA_ARCHIVO, "w") as f:
        json.dump(usuarios, f, indent=4)
