class Optimal:

    def __init__(self, cantidad_marcos, referencias):

        self.cantidad_marcos = cantidad_marcos
        self.referencias = referencias

        self.memoria = []

        self.page_faults = 0
        self.hits = 0
        self.paso = 1

        self.historial = []

    def acceder_pagina(self, pagina, posicion_actual):

        if pagina in self.memoria:

            self.hits += 1

            resultado = "HIT"

        else:

            self.page_faults += 1

            if len(self.memoria) < self.cantidad_marcos:

                self.memoria.append(pagina)

            else:

                futura_referencia = self.referencias[posicion_actual + 1:]

                indice_a_reemplazar = -1
                mayor_distancia = -1

                for i in range(len(self.memoria)):

                    pagina_memoria = self.memoria[i]

                    if pagina_memoria not in futura_referencia:

                        indice_a_reemplazar = i

                        break

                    distancia = futura_referencia.index(pagina_memoria)

                    if distancia > mayor_distancia:

                        mayor_distancia = distancia
                        indice_a_reemplazar = i

                self.memoria[indice_a_reemplazar] = pagina

            resultado = "PAGE FAULT"

        self.historial.append(
            {
                "paso": self.paso,
                "pagina": pagina,
                "memoria": self.memoria.copy(),
                "resultado": resultado
            }
        )

        self.paso += 1