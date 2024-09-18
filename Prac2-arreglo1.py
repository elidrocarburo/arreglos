import numpy as np
import pandas as pd
import time

inicio = time.time()

fila = int(input("¿Cuántas materias desea ingresar?: "))
columna = int(input("¿Cuántos alumnos desea ingresar?: "))
fila1 = int(input("Ingrese el número de materia para buscar una calificación: "))
columna1 = int(input("Ahora ingrese el número de alumno para hacer la búsqueda: "))

arreglo = np.random.randint(0,101, size=(fila,columna))

materias = [f"Materia {i+1}" for i in range(fila)]
alumnos = [f"Alumno {i+1}" for i in range(columna)]

tabla = pd.DataFrame(arreglo, index=materias, columns=alumnos)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

ind_fila = int(fila1)-1
ind_columna = int(columna1) -1

indice = tabla.iloc[ind_fila,ind_columna]

print("Lista de Calificaciones")
print(tabla)
print(indice)

fin = time.time()
tiempo = fin - inicio
print(f"\nTiempo de ejecución: {tiempo: .4f} s")