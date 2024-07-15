# Programa-de-Entrenamiento
---> A continuacion los requerimientos del trabajo realizado...

Un centro de entrenamiento deportivo necesita un programa que le permita operar con los diferentes programas avanzados
que tiene disponibles para los deportistas que entrenan en ese centro. De cada Programa, se tiene una clave
de identificación (una cadena que puede tener dígitos y caracteres), el nombre del entrenador a cargo de ese programa,
 la descripción del contenido de ese programa (una cadena con un texto terminado en punto y con palabras separadas
 por un blanco. Por ejemplo: "Entrenamiento intensivo en judo para varones de menos de 70 kilos."
", etc.), la cantidad de deportistas registrados para ese programa (puede valer cero), un número entre 1 y 50 que
indica el deporte para ese programa (por ejemplo: 1: fútbol, 2: basquet, etc.), y otro número pero entre 0 y 9 para
indicar el nivel de entrenamiento ofrecido en ese programa (por ejemplo: 0: de alta competencia, 1: de recuperación, 2:
de competencia inicial, etc.).
En base a lo anterior, desarrollar un programa completo que disponga al menos de dos módulos:
• En uno de ellos, definir la clase Programa que represente al registro a usar en el programa, y las funciones
básicas para operar con registros de ese tipo.
En otro módulo, incluir el programa principal y las funciones generales que sean necesarias. Aplique las validaciones
 que considere necesarias. El programa debe basarse en un menú de opciones para desarrollar las siguientes tareas:

1. Generar un archivo binario de registros que contenga los datos de todos los programas disponibles en el centro.
Puede generarlo cargando los datos en forma manual o aleatoria. No se requiere que el archivo permanezca ordenado
mientras se carga, ni tampoco que se ordene de ninguna forma al terminar el proceso. Debe considerar que esta opción
puede ser invocada varias veces a lo largo del programa, y que en cada ejecución pueden agregarse tantos registros como desee el operador, sin eliminar los datos que ya estaban cargados. Observación:
NO CARGUE LOS DATOS EN UN ARREGLO PARA DESPUÉS GRABARLOS EN EL ARCHIVO: DIRECTAMENTE CARGUE LOS DATOS EN EL ARCHIVO.
SERÁ CONSIDERADA INCORRECTA CUALQUIER SOLUCIÓN BASADA EN GENERAR PRIMERO UN ARREGLO Y LUEGO GRABAR
ESE ARREGLO EN EL ARCHIVO.

2. Muestre el archivo generado, a razón de un registro por línea en la consola de salida. Al final del listado, muestre una línea adicional en la que se informe cuántos registros se mostraron.

3. A partir del archivo cargado en el punto 1, genere un arreglo de registros con todos los programas del archivo cuya
cantidad de deportistas registrados sea diferente de cero. El arreglo debe mantenerse ordenado de menor a mayor en todos momento durante el proceso de creación, de acuerdo al valor del campo clave de identificación.
Cada vez que esta opción se elija, el arreglo debe volver a crearse desde cero, eliminando los datos que pudiese
contener anteriormente. NO GENERE ESTE ARREGLO DIRECTAMENTE EN LA OPCIÓN 1, AL MISMO TIEMPO QUE GRABA EL ARCHIVO.
 DEBE RESOLVER ESTE PEDIDO CON UNA OPCIÓN SEPARADA EN EL MENÚ DE OPCIONES.

4. Muestre el arreglo generado en el punto anterior, a razón de un registro por línea en la pantalla.

5. Determine si existe en el arreglo un programa en el que el nombre del entrenador coincida con el valor nom que
se carga por teclado. Si existe, detenga la búsqueda al primero que encuentre y muestre todos sus datos. Si no existe,
 cargue por teclado (o genere en forma aleatoria) un registro nuevo con los datos del programa, asigne el nombre nom del entrenador en el campo correspondiente, y agregue en el arreglo el nuevo registro, manteniendo el orden por clave de identificación.

6. Determine si existe en el arreglo un programa en que la clave de identificacion sea igual a la pasada por teclado.

7. Determine la cantidad acumulada de deportistas  que estan registrados para cada uno de los posibles deportes por
cada nivel de entrenamiento posible, muestre solo los resultados mayores a n
