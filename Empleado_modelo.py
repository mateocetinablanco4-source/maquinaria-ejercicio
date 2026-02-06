class Empleado_modelo:
    def __init__(self, nombre, apellido, cedula, telefono):
        self.nombre_empleado = nombre
        self.apellido_empleado = apellido
        self.cedula_empleado = cedula
        self.telefono_empleado = telefono
        
    def set_nombre_empleado(self, nuevo_nombre, eliminar_obj):
        self.nombre_empleado = nuevo_nombre
        self.eliminar_obj = eliminar_obj
    
    def get_nombre_empleado(self):
        return self.nombre_empleado
    
    def set_apellido_empleado(self, nuevo_apellido):
        self.apellido_empleado = nuevo_apellido
    
    def get_apellido_empleado(self):
        return self.apellido_empleado
    
    def set_cedula_empleado(self, nueva_cedula):
        self.cedula_empleado = nueva_cedula
    
    def get_cedula_empleado(self):
        return self.cedula_empleado
    
    def set_telefono_empleado(self, nuevo_telefono):
        self.telefono_empleado = nuevo_telefono
    
    def get_telefono_empleado(self):
        return self.telefono_empleado
    
    def ver_info(self):
        info = "Nombre empleado: " + self.nombre_empleado + " Apellido empleado: " + self.apellido_empleado
        info = info + " Cedula empleado: " + self.cedula_empleado  + " Telefono empleado: " + self.telefono_empleado