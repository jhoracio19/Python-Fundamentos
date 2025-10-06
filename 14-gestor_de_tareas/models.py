
class Tarea:
    
    def __init__(self, titulo, descripcion, prioridad):
        self.validar_titulo(titulo)
        self.validar_prioridad(prioridad)
        
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad.capitalize()
        self.estado = 'Pendiente'
    
    def validar_titulo(self, titulo):
        if titulo == '':
            raise TituloInvalidoError(titulo)
    
    def validar_prioridad(self, prioridad):
        if prioridad not in ['alta', 'media', 'baja']:
            raise PrioridadInvalidaError(prioridad)
    
    def marcar_completado(self):
        self.estado = 'Completado'


class TituloInvalidoError(Exception):
    def __init__(self, titulo, mensaje = "El titulo no puede ir vacio"):
        self.titulo = titulo
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class PrioridadInvalidaError(Exception):
    def __init__(self, prioridad, mensaje = "La prioridad debe ser 'alta', 'media', 'baja' "):
        self.prioridad = prioridad
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class MarcaInvalidaError(Exception):
    def __init__(self, tarea, mensaje='No se puede marcar una tarea inexistene'):
        self.tarea = tarea
        self.mensaje = mensaje
        super().__init__(self.mensaje)        