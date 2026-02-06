class base_datos_empleados:
    def __init__(self):

        
        self.db_empleados_listas = []
    
    def guardar_empleado(self, obj_empleados):

        self.db_empleados_lista.append(obj_empleados)

        return True
    def guardar_varios_empleados(self, varios_odj):

        self.db_empleados_listas.extend(varios_odj)


        #print("xxxx: " , self.db_empleado_lista)
        

        #print("aaaa: " , self.db_empleado_lista[0].get_nombre_empleado())
    
    def imprimir_info(self):
        for i in range(len(self.db_empleado_lista)):

            nombre = self.db_empleado_lista[i].get_nombre_empleado()

            apellido = self.db_empleado_lista[i].get_apellido_empleado()

            cedula = self.db_empleado_lista[i].get_cedula_empleado()

            
            print(f"nombre empleado: {nombre} - apellido: {apellido} - cedula: {cedula}")