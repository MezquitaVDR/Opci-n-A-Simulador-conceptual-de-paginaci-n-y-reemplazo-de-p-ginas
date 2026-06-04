# Simulador de Paginación

Proyecto desarrollado en Python para simular algoritmos de reemplazo de páginas utilizados en sistemas operativos.

## Algoritmos implementados

* FIFO (First In First Out)
* LRU (Least Recently Used)
* CLOCK (Reloj)
* OPTIMAL (Óptimo)

## Funcionalidades

* Simulación paso a paso de cada algoritmo.
* Visualización del estado de la memoria en cada acceso.
* Conteo de Hits y Page Faults.
* Comparación de los cuatro algoritmos.
* Identificación automática del algoritmo más eficiente para la secuencia de páginas ingresada.

## Requisitos

* Python 3.x
* Tkinter (incluido en Python)

## Archivos del proyecto

* `main.py`: Archivo principal.
* `interfaz.py`: Interfaz gráfica del simulador.
* `fifo.py`: Implementación del algoritmo FIFO.
* `lru.py`: Implementación del algoritmo LRU.
* `clock.py`: Implementación del algoritmo CLOCK.
* `optimal.py`: Implementación del algoritmo OPTIMAL.
* `tabla_paginas.py`: Traducción de direcciones virtuales a físicas.

## Ejecución

Ejecutar el siguiente comando:

```bash
python main.py
```

## Autores

Proyecto desarrollado para la asignatura Manejo de Estructuras de Datos.

Universidad de El Salvador
Facultad Multidisciplinaria de Occidente
Ingeniería en Desarrollo de Software
