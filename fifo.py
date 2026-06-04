class FIFO:

    def __init__(self, cantidad_marcos):
        self.cantidad_marcos = cantidad_marcos
        self.memoria = []

        self.page_faults = 0
        self.hits = 0
        self.paso = 1

        self.historial = []

    def acceder_pagina(self, pagina):

        if pagina in self.memoria:

            self.hits += 1
            resultado = "HIT"

        else:

            self.page_faults += 1

            if len(self.memoria) < self.cantidad_marcos:
                self.memoria.append(pagina)
            else:
                self.memoria.pop(0)
                self.memoria.append(pagina)

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