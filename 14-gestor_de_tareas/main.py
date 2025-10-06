from models import Tarea, TituloInvalidoError, PrioridadInvalidaError, MarcaInvalidaError
from utils import cargar_tareas, guardar_tareas, actualizar_tareas

def agregar_tarea():
    try:
        titulo= input("Título de la tarea: ").strip()
        descripcion = input("Descripción de la tarea: ").strip()
        prioridad = input("Prioridad (alta, media, baja): ").strip().lower()
        
        nueva_tarea = Tarea(titulo, descripcion, prioridad)
        guardar_tareas(vars(nueva_tarea))
        print("\n Tarea agregada correctamente. \n")
        
    except (TituloInvalidoError, PrioridadInvalidaError, MarcaInvalidaError) as e:
        print(f'\nError: {e}\n')

def listar_tareas():
    tareas = cargar_tareas()
    if not tareas:
        print("\nNo hay tareas registradas. \n")
        return
    
    print("\n--- Lista de Tareas ---")
    for i, t in enumerate(tareas, start=1):
        print(f"{i}.[{t['estado']}] {t['titulo']} - {t['descripcion']}")
    print('--------------------')

def marcar_completada():
    tareas = cargar_tareas()
    if not tareas:
        print("\n📭 No hay tareas registradas.\n")
        return

    listar_tareas()
    try:
        index = int(input("Ingresa el número de la tarea a marcar como completada: ")) - 1
        if 0 <= index < len(tareas):
            tareas[index]['estado'] = "Completada"
            actualizar_tareas(tareas)
            print(f"\n✅ Tarea '{tareas[index]['titulo']}' marcada como completada.\n")
        else:
            raise MarcaInvalidaError(index)
    except ValueError:
        print("\n⚠️ Ingresa un número válido.\n")
    except MarcaInvalidaError as e:
        print(f"\n❌ Error: {e}\n")


def ver_por_prioridad():
    tareas = cargar_tareas()
    if not tareas:
        print("\n📭 No hay tareas registradas.\n")
        return

    prioridad = input("Filtrar por prioridad (alta, media, baja): ").strip().lower()
    filtradas = [t for t in tareas if t['prioridad'].lower() == prioridad]

    if not filtradas:
        print(f"\n❌ No hay tareas con prioridad '{prioridad}'.\n")
        return

    print(f"\n--- Tareas con prioridad {prioridad.capitalize()} ---")
    for i, t in enumerate(filtradas, start=1):
        print(f"{i}. [{t['estado']}] {t['titulo']} - {t['descripcion']}")
    print("----------------------------\n")


def menu():
    while True:
        print("=== Gestor de Tareas ===")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Ver tareas por prioridad")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            marcar_completada()
        elif opcion == "4":
            ver_por_prioridad()
        elif opcion == "5":
            print("\n👋 Saliendo del gestor. ¡Hasta luego!\n")
            break
        else:
            print("\n❌ Opción no válida.\n")


if __name__ == "__main__":
    menu()