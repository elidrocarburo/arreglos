# arreglos
Repositorio del código de arreglos
<p>El siguiente programa es un arreglo bidimensional, el cual pide el ingreso de materias como filas y alumnos como columnas, ya que es una lista de calificaciones.</p>
<p>Lo primero que hice fue importar librerías para facilitar la creación de la matriz.</p>
<ul>
  <li>Numpy: es una librería para el manejo de grandes conjuntos de datos, su sintaxis es import numpy as np, el np puede ser cualquier nombre que se le desee, pero es para que puedas manejarlo dentro de tu código. En este caso lo utilicé para la generación de números aleatorios dentro de cierto rango para no estar introduciéndolos por mi cuenta</li>
  <li>Pandas: es una librería para la estructura de datos, para este caso me permitió poner de manera automatizada el número de materia y alumno gracias a que se maneja por medio de índices, y de igual manera permite el acceso a los datos. Su sintaxis es import pandas as pd, donde el pd es el nombre que uno desee ponerle, pero es para que puedas manejarlo dentro del código.</li>
  <li>Times: la librería times sirve como un cronómetro para tu programa, calculando el tiempo el cual va ejecutando el programa, su sintaxis es import time. Yo lo usé para contar en cuánto tiempo me arroja mi tabla de calificaciones.</li>
</ul>
<p>Siguiendo con el código, como quiero que el usuario introduzca la cantidad que quiera de materias y de alumnos, decidí usar 4 inputs para la introducción de las materias y alumnos y el localizar la calificación de una materia de un cierto alumno.</p>
<p>arreglo = np.random.randint(0,101, size=(fila,columna)) sirve para el llenado automático del arreglo de números aleatorios, pero dentro de un rango.</p>
<p>Las siguientes líneas de código me crearán la lista de nombres para las filas y columnas:</p>
<ul>
  <li>materias = [f"Materia {i+1}" for i in range(fila)]</li>
  <li>alumnos = [f"Alumno {i+1}" for i in range(columna)]</li>
</ul>
<p>tabla = pd.DataFrame(arreglo, index=materias, columns=alumnos) y con las filas y columnas nombradas, me permitirá crear el arreglo con nombres gracias a la librería pandas. El DataFrame se usó ya que es una estructura de dos dimensiones.</p>
<p>Las siguientes líneas de código me ayudaron a que me despliegue todos los resultados del arreglo, ya que, de lo contrario, me mostraría pocos elementos ya que estaría resumidos con un “…”, y de igual manera, me ayudé con la librería pandas:</p>
<ul>
  <li>pd.set_option('display.max_rows', None)</li>
  <li>pd.set_option('display.max_columns', None)</li>
</ul>
<p>Las siguientes líneas de código son para la localización de la calificación por medio de índices, el -1 ajusta la posición al estar basados en 0:</p>
<ul>
  <li>ind_fila = int(fila1)-1</li>
  <li>ind_columna = int(columna1) -1</li>
</ul>
<p>Y la línea indice = tabla.iloc[ind_fila,ind_columna] es para poder localizar el valor e imprimirlo.</p>
<p>Las últimas líneas son la impresión del texto “Lista de calificaciones”, la tabla y el valor que hayamos querido localizar.</p>
<p>Tanto al inicio como al final del programa, hice uso de la librería times, declarándola con inicio y fin, con la sintaxis time.time(), la cual me va a servir para el cálculo del inicio de ejecución del programa y al final, haciendo una resta de ambos tiempos para que me ayude a calcular el tiempo después de que terminó de ejecutarse, para que pueda terminar imprimiéndolo.</p>
<ul>
  <li>inicio = time.time()</li>
  <li>fin = time.time()</li>
  <li>tiempo = fin – inicio</li>
</ul>
