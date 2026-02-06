class EMPLEADOS_MODELOS:
    def __init__(self):

        self.hora_fin = 0 

        self.hora_inicio =0

        self.maquina_asignada=""

        self.cod_empleado =""

    def set_codigo(self,nuevo_codigo):

        self.cod_empleado = nuevo_codigo
    
    def get_codigo(self):

        return self.cod_empleado
    
    def set_nombre(self,nuevo_nombre):

        self.cod_empleado=nuevo_nombre
    
    def get_codigo(self):
        
        return self.cod_empleado