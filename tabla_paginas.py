class TablaPaginas:

    def __init__(self, tamaño_pagina, tabla):
        self.tamaño_pagina = tamaño_pagina
        self.tabla = tabla

    def traducir_direccion(self, direccion_virtual):

        numero_pagina = direccion_virtual // self.tamaño_pagina

        desplazamiento = direccion_virtual % self.tamaño_pagina

        if numero_pagina not in self.tabla:
            print("PAGE FAULT")
            return

        marco = self.tabla[numero_pagina]

        direccion_fisica = marco * self.tamaño_pagina + desplazamiento

        print("\n===== TRADUCCIÓN =====")
        print("Dirección virtual:", direccion_virtual)
        print("Número de página:", numero_pagina)
        print("Desplazamiento:", desplazamiento)
        print("Marco asignado:", marco)
        print("Dirección física:", direccion_fisica)