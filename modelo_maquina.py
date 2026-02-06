class Empleado_modelo:
    def __init__(self, nombre, modelo, codigo, estado):
        self.nombre_maquina = nombre
        self.modelo_maquina = modelo
        self.codigo_maquina = codigo
        self.estado_maquina = estado
        
    def set_nombre_maquina(self,nuevo_nombre, elimina_obj):
        self.nombre_maquina = nuevo_nombre
        self.elimina_obj = elimina_obj
    
    def get_nombre_maquina(self):        
        return self.nombre_maquina
    
    def set_modelo_maquina(self, nuevo_modelo):
        self.modelo_maquina = nuevo_modelo
    
    def get_modelo_maquina(self,):
        return self.modelo_maquina
    
    def set_codigo_maquina(self, nuevo_codigo):
        self.set_codigo_maquina = nuevo_codigo
        
    def get_codigo_maquina(self,):
        return self.set_codigo_maquina
    
    def set_estado_maquina(self,nuevo_estado):
        self.estado_maquina = nuevo_estado
    
    def get_estado_maquina(self,):
        return self.estado_maquina
    
    def ver_info(self):
        info = "Nombre maquina: " +self.nombre_maquina + "Modelo maquina: " + self.modelo_maquina
        info = info+ "Código maquina" + self.codigo_maquina + " Estado maquina: " + self.estado_maquina