from models import Usuario, EdadInvalidaError, CorreoInvalidoError, PasswordInvalidaError
from utils import cargar_usuarios, guardar_usuario

def registrar_usuario():
    try:
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        correo = input("Correo: ")
        password = input("Contraseña: ")

        nuevo_usuario = Usuario(nombre, edad, correo, password)
        guardar_usuario(vars(nuevo_usuario))
        print("\n✅ Usuario registrado correctamente.\n")

    except (EdadInvalidaError, CorreoInvalidoError, PasswordInvalidaError) as e:
        print(f"\n❌ Error: {e}\n")
    except ValueError:
        print("\n⚠️ La edad debe ser un número.\n")


def listar_usuarios():
    usuarios = cargar_usuarios()
    if not usuarios:
        print("\n📭 No hay usuarios registrados.\n")
        return
    print("\n--- Usuarios Registrados ---")
    for i, u in enumerate(usuarios, start=1):
        print(f"{i}. {u['nombre']} | {u['edad']} años | {u['correo']}")
    print("-----------------------------\n")


def menu():
    while True:
        print("=== Sistema de Registro de Usuarios ===")
        print("1. Registrar usuario")
        print("2. Ver usuarios registrados")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            listar_usuarios()
        elif opcion == "3":
            print("\n👋 Saliendo del sistema...")
            break
        else:
            print("\n❌ Opción no válida.\n")


if __name__ == "__main__":
    menu()
