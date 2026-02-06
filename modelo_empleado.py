class empleado_modelo:
    def __init__(self, nombre, apellido, cedula, celular):

        self.nombre_empleado=nombre

        self.apellido_empleado=apellido

        self.cedula_empleado=cedula
        
        self.celular_empleado=celular
    
    def set_nombre_empleado(self,nuevo_nombre):

        self. nombre_empleado=nuevo_nombre
    
    def get_nombre_empleado(self,):   

        return self.nombre_empleado
    
    def set_apellido_empleado(self, nuevo_apellido):

        self.apellido_empleado  =nuevo_apellido
    
    def get_apellido_empleado(self,):

        return self.apellido_empleado
    
    def set_cedula_empleado(self, nuevo_cedula):

        self .cedula_empleado = nuevo_cedula
        
    def get_cedula_empleado(self,):

        return self.cedula_empleado
    
    def set_celular_empleado(self,nuevo_celular):

        self. celular_empleado=nuevo_celular
    
    def get_celular_empleado(self,):

        return self.cedula_empleado
    
    def ver_info(self):

        info="nombre empleado: " +self. nombre_empleado + "apellido empleado"
        
        info=info+ "cedula empleado" + self. cedula_empleado + "telefono empleado " + self.celular_empleado