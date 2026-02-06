from base_datos_empleados import base_datos_empleados

from modelo_empleado import modelo_empleado

# creo la base de dotos de empleados
obj_db_empleado_lista = base_datos_empleados()

#creo el objeto que voy a guardar
obj_empleado = modelo_empleado("Mateo" , " Cetina" , "8578545" , "3154875248")
obj_empleado2 = modelo_empleado("maria" , "Blanco" , "5483554" , "916560248")

#creo una lista para guardar masivamente
lista_nuevos_empleados = [obj_empleado2, obj_empleado]

# llamo el metodo de la  base de datos que guarda la objeto

obj_db_empleado_lista.guardar_empleados(obj_empleado)#guardando un obj

obj_db_empleado_lista.guardar_empleado(obj_empleado2)


obj_db_empleado_lista.extender_varios_empleados(lista_nuevos_empleados)

#imprimo toda la lista de empleados
obj_db_empleado_lista.imprimir_info
