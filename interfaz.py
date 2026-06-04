import tkinter as tk
from tkinter import ttk

from fifo import FIFO
from lru import LRU
from clock import Clock
from optimal import Optimal


class Interfaz:

    def __init__(self):

        self.ventana = tk.Tk()
        self.ventana.title("Simulador de Paginación")
        self.ventana.geometry("1000x700")

        # ===== Entradas =====

        tk.Label(
            self.ventana,
            text="Cantidad de marcos"
        ).pack()

        self.entry_marcos = tk.Entry(self.ventana)
        self.entry_marcos.insert(0, "3")
        self.entry_marcos.pack()

        tk.Label(
            self.ventana,
            text="Secuencia de páginas"
        ).pack()

        self.entry_paginas = tk.Entry(
            self.ventana,
            width=50
        )

        self.entry_paginas.insert(
            0,
            "7,0,1,2,0,3,0,4,2,3"
        )

        self.entry_paginas.pack()

        tk.Label(
            self.ventana,
            text="Mostrar simulación de"
        ).pack()

        self.combo = ttk.Combobox(
            self.ventana,
            values=[
                "FIFO",
                "LRU",
                "CLOCK",
                "OPTIMAL"
            ]
        )

        self.combo.current(0)
        self.combo.pack()

        tk.Button(
            self.ventana,
            text="Simular",
            command=self.simular
        ).pack()

        # ===== Tabla principal =====

        tk.Label(
            self.ventana,
            text="Simulación paso a paso"
        ).pack()

        self.tabla = ttk.Treeview(
            self.ventana,
            columns=(
                "Paso",
                "Página",
                "Memoria",
                "Resultado"
            ),
            show="headings",
            height=10
        )

        self.tabla.heading("Paso", text="Paso")
        self.tabla.heading("Página", text="Página")
        self.tabla.heading("Memoria", text="Memoria")
        self.tabla.heading("Resultado", text="Resultado")

        self.tabla.pack(fill="x")

        # ===== Tabla comparación =====

        tk.Label(
            self.ventana,
            text="Comparación de algoritmos"
        ).pack()

        self.tabla_comparacion = ttk.Treeview(
            self.ventana,
            columns=(
                "Algoritmo",
                "Hits",
                "Page Faults"
            ),
            show="headings",
            height=4
        )

        self.tabla_comparacion.heading(
            "Algoritmo",
            text="Algoritmo"
        )

        self.tabla_comparacion.heading(
            "Hits",
            text="Hits"
        )

        self.tabla_comparacion.heading(
            "Page Faults",
            text="Page Faults"
        )

        self.tabla_comparacion.pack(fill="x")
        # ===== Mejor algoritmo =====

        self.label_mejor = tk.Label(
            self.ventana,
            text="",
            font=("Arial", 12, "bold"),
            fg="blue"
        )

        self.label_mejor.pack(pady=10)
        self.ventana.mainloop()

    def simular(self):

        # Limpiar tablas

        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for fila in self.tabla_comparacion.get_children():
            self.tabla_comparacion.delete(fila)

        marcos = int(self.entry_marcos.get())

        referencias = list(
            map(
                int,
                self.entry_paginas.get().split(",")
            )
        )

        # ===== Ejecutar los 4 algoritmos =====

        fifo = FIFO(marcos)

        for pagina in referencias:
            fifo.acceder_pagina(pagina)

        lru = LRU(marcos)

        for pagina in referencias:
            lru.acceder_pagina(pagina)

        clock = Clock(marcos)

        for pagina in referencias:
            clock.acceder_pagina(pagina)

        optimal = Optimal(
            marcos,
            referencias
        )

        for i in range(len(referencias)):
            optimal.acceder_pagina(
                referencias[i],
                i
            )

        # ===== Mostrar algoritmo seleccionado =====

        algoritmo = self.combo.get()

        if algoritmo == "FIFO":
            simulador = fifo

        elif algoritmo == "LRU":
            simulador = lru

        elif algoritmo == "CLOCK":
            simulador = clock

        else:
            simulador = optimal

        for registro in simulador.historial:

            self.tabla.insert(
                "",
                tk.END,
                values=(
                    registro["paso"],
                    registro["pagina"],
                    str(registro["memoria"]),
                    registro["resultado"]
                )
            )

        # ===== Tabla comparativa =====

        self.tabla_comparacion.insert(
            "",
            tk.END,
            values=("FIFO", fifo.hits, fifo.page_faults)
        )

        self.tabla_comparacion.insert(
            "",
            tk.END,
            values=("LRU", lru.hits, lru.page_faults)
        )

        self.tabla_comparacion.insert(
            "",
            tk.END,
            values=("CLOCK", clock.hits, clock.page_faults)
        )

        self.tabla_comparacion.insert(
            "",
            tk.END,
            values=("OPTIMAL", optimal.hits, optimal.page_faults)
        )

        # ===== Determinar el mejor algoritmo =====

        algoritmos = {
            "FIFO": fifo.page_faults,
            "LRU": lru.page_faults,
            "CLOCK": clock.page_faults,
            "OPTIMAL": optimal.page_faults
        }

        menor_fallos = min(algoritmos.values())

        mejores = [
            nombre
            for nombre, fallos in algoritmos.items()
            if fallos == menor_fallos
        ]

        self.label_mejor.config(
            text=f"🏆 Mejor(es): {', '.join(mejores)} con {menor_fallos} Page Faults"
        )


Interfaz()