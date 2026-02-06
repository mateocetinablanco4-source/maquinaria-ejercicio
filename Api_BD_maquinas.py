class Api_BD_maquinas:
    def __init__(self):
        self.Api_maquinas = [
            ["Código", "Nombre Maquina", "Modelo", "Estado Maquina"],
            ["Cod 1921", "Brazo mecánico", "x102", "Apagada"],
            ["Cod 1234", "Cinta transportadora", "zx400", "Requiere mantenimiento"],
            ["Cod 5564", "Monobrazo", "j102", "Encendida"],
        ]
    
    def imprimir_info(self):
        for i in range(len(self.Api_maquinas)):
            print(self.Api_maquinas[i])
    
    def buscar_info(self):
        return self.Api_maquinas[0] [1]
    
    def guardar_maquinas(self, obj_maquinas):
        self.Api_maquinas.append(obj_maquinas)
        return True

    def extender_varias_maquinas(self, varias_odj):
        self.Api_maquinas.extend(varias_odj)
    
    def agregar_info_maquinas(self, dato_i, infor_obj):
        self.Api_maquinas.insert(dato_i, infor_obj)
        
    def borrar_info_maquinas(self,borrar_obj,dato_i):
        self.Api_maquinas.remove("Code")
        
    def devolver_info_maquinas(self, elimina_obj,devuelve_obj):
        data = self.Api_maquinas.pop("Brazo mecánico")
        
    def mover_info_maquinas(self,dato_modelo_maquina):
        aux = self.Api_maquinas.index(dato_modelo_maquina) 
        
    def contar_info_maquinas(self,dato_monobrazo):
        self.Api_maquinas.count(dato_monobrazo)
        
    def obtener_modelo(self,maquinas):
        return maquinas.get_nombre_modelo()
    
    def sort_maquinas(self):
        self.Api_maquinas.sort(key = self.obtener_modelo)
        return True
    
    def revertir_maquinas (self):
        self.Api_maquinas.reverse(key = self.obtener_modelo)
        return True