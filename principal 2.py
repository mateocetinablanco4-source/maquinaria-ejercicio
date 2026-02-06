from Base_datos_empleados import Base_datos_empleados
from Empleado_modelo import Empleado_modelo


#creo la base de datos de empleados
obj_db_empleado_lista = Base_datos_empleados()


#creo el objeto que voy a guardar
obj_empleado1 = Empleado_modelo("Mateo", "Jose", "123456789", "321-8906543")
obj_empleado2 = Empleado_modelo("Breiner", "Josue", "987654321", "312-4567890")


#creo una lista para guardar masivamente
lista_nuevos_empleados = [obj_empleado2, obj_empleado1]


#llamo al metodo para guardar el empleado
obj_db_empleado_lista.guardar_empleado(obj_empleado1)
obj_db_empleado_lista.guardar_empleado(obj_empleado2)
lista_nuevos_empleados = [obj_empleado1, obj_empleado2]
obj_db_empleado_lista.extender_varios_empleados(lista_nuevos_empleados)


#limpiar toda la lista de empleados
obj_db_empleado_lista.imprimir_info()


#creamos la bd de maquinas
bd_maquinas = Api_BD_maquinas


#creamos objetos de maquinas
maquina1 = modelo_maquina("Brazo mecánico", "x102", "Apagada")
maquina2 = modelo_maquina("Cinta transportadora", "zx400", "Requiere mantenimiento")


#guardamos
bd_maquinas.guardar_maquinas(maquina1)
bd_maquinas.guardar_maquinas(maquina2)


#mostrar resultados
bd_maquinas.imprimir_info()