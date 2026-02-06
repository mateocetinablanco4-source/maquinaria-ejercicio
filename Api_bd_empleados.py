class Api_BD_maquinas:
    
    def __init__(self):

        self.Api_maquina = [
            ["codigo","nombre maquina","modelo maquina","estado maquina"],

            ["code 1234","brazo mecanico","x200","apagada"],

            ["code 2134","cinta transportadora","zx400","requiere mantenimiento"],

            ["code 3214","monobrazo","jk100","encendida"],
            
        ]
        
    def imprimir_info(self):

        for i in range(len(self. Api_maquina)):

            print(self.Api_maquina[i])
            
    def buscar_info(self):
        
        return self.Api_maquina[0][1]