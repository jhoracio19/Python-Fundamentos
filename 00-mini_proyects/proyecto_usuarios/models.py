# Crear un programa completo que permita:
# Registrar usuarios (nombre, edad, correo, contraseña).
# Validar los datos (edad mínima, formato del correo, contraseña segura).
# Guardar los datos en un archivo JSON.
# Listar usuarios registrados desde el archivo.
# Manejar errores personalizados (por ejemplo, edad o correo inválido).
# Organizar el código en módulos (por ejemplo: main.py, models.py, utils.py, etc.).
# (Opcional Pro) Generar un PDF con el resumen de usuarios registrados usando fpdf2.

class Usuario():
    
    def __init__(self, nombre, edad, correo, password):
        self.validar_edad(edad)
        self.validar_correo(correo)
        self.validar_password(password)
        
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.password = password
    
    def validar_edad(self, edad):
        if edad < 18:
            raise EdadInvalidaError(edad)
    
    def validar_correo(self, correo):
        if "@" not in correo or '.' not in correo.split('@')[-1]:
            raise CorreoInvalidoError(correo)
    
    def validar_password(self, password):
        if len(password) < 6:
            raise PasswordInvalidaError(password)


class EdadInvalidaError(Exception):
    
    def __init__(self, edad, mensaje="La edad debe ser mayor o igual a 18."):
        self.edad = edad
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class CorreoInvalidoError(Exception):
    
    def __init__(self, correo, mensaje="Correo con formato no válido"):
        self.correo = correo
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class PasswordInvalidaError(Exception):
    
    def __init__(self, password, mensaje="La contraseña debe de ser de al menos 6 caracteres."):
        self.password = password
        self.mensaje = mensaje
        super().__init__(self.mensaje)