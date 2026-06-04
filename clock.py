class Clock:

    def __init__(self, cantidad_marcos):

        self.cantidad_marcos = cantidad_marcos

        self.memoria = [None] * cantidad_marcos
        self.bits = [0] * cantidad_marcos

        self.puntero = 0

        self.page_faults = 0
        self.hits = 0
        self.paso = 1

        self.historial = []

    def acceder_pagina(self, pagina):

        if pagina in self.memoria:

            indice = self.memoria.index(pagina)

            self.bits[indice] = 1

            self.hits += 1

            resultado = "HIT"

        else:

            self.page_faults += 1

            while True:

                if self.memoria[self.puntero] is None:

                    self.memoria[self.puntero] = pagina
                    self.bits[self.puntero] = 1

                    self.puntero = (self.puntero + 1) % self.cantidad_marcos

                    break

                elif self.bits[self.puntero] == 0:

                    self.memoria[self.puntero] = pagina
                    self.bits[self.puntero] = 1

                    self.puntero = (self.puntero + 1) % self.cantidad_marcos

                    break

                else:

                    self.bits[self.puntero] = 0

                    self.puntero = (self.puntero + 1) % self.cantidad_marcos

            resultado = "PAGE FAULT"

        self.historial.append(
            {
                "paso": self.paso,
                "pagina": pagina,
                "memoria": self.memoria.copy(),
                "bits": self.bits.copy(),
                "resultado": resultado
            }
        )

        self.paso += 1