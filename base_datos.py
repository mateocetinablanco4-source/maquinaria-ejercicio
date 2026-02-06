class Api_BD:
    
    def __init__(self):

        self. Api_datos = []
    
    def guardar_empleado(self,obj_nuevo_epleado):

        self.Api_datos.append(obj_nuevo_epleado)
        
    def imprimir_Api(self):

        for empleado in self.Api_datos:
            
            print(empleado)