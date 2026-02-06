class Base_datos_empleados:
    def __init__(self):
        #este es un array
        self.db_empleados_lista = [
            ["Mateo", "Jose"]
            ["Breiner", "Josue"]
        ]
        
    def guardar_empleado(self, obj_empleado):
        self.db_empleados_lista.append(obj_empleado)
        return True

    def extender_varios_empleados(self, varios_obj):
        self.db_empleados_lista.extend(varios_obj)
        print("xxxx: ", self.db_empleado_lista)
        print("aaaa: ", self.db_empleado_lista[0].get_nombre_empleado())

    def agregar_info_empleado(self, dato_i, info_obj):
        self.db_empleado_lista.insert(dato_i, info_obj)
        
    def eliminar_info_empleado(self,eliminar_obj,dato_i):
        self.db_empleado_lista.remove("Mateo")
        
    def eliminar_info_empleado(self, eliminar_obj,devolver_obj):
        data = self.db_empleado_lista.pop("Breiner")
        
    def mover_info_empleado(self,dato_nombre):
        aux = self.db_empleado_lista.index(dato_nombre) 
        
    def contar_info_empleados(self,dato_andres):
        self.db_empleado_lista.count(dato_andres)
        
    def obtener_nombre(self,empleados):
        return empleados.get_nombre_empleado()
    
    def sort_empleados(self):
        self.db_empleado_lista.sort(key = self.obtener_nombre)
        return True
    
    def revertir_empleados(self):
        self.db_empleado_lista.reverse(key = self.obtener_nombre)
        return True
        
    def imprimir_info(self):
        for i in range(len(self.db_empleados_lista)):
            print(self.db_empleados_lista[i].ver_info_empleado())   