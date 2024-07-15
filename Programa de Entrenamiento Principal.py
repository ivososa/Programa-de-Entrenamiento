'''
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
puede ser invocada varias veces a lo largo del programa, y que en cada ejecución pueden agregarse tantos registros como
 desee el operador, sin eliminar los datos que ya estaban cargados. Observación:
NO CARGUE LOS DATOS EN UN ARREGLO PARA DESPUÉS GRABARLOS EN EL ARCHIVO: DIRECTAMENTE CARGUE LOS DATOS EN EL ARCHIVO.
SERÁ CONSIDERADA INCORRECTA CUALQUIER SOLUCIÓN BASADA EN GENERAR PRIMERO UN ARREGLO Y LUEGO GRABAR
ESE ARREGLO EN EL ARCHIVO.

2. Muestre el archivo generado, a razón de un registro por línea en la consola de salida. Al final del listado, muestre
una línea adicional en la que se informe cuántos registros se mostraron.

3. A partir del archivo cargado en el punto 1, genere un arreglo de registros con todos los programas del archivo cuya
cantidad de deportistas registrados sea diferente de cero. El arreglo debe mantenerse ordenado de menor a mayor en todos
 momento durante el proceso de creación, de acuerdo al valor del campo clave de identificación.
Cada vez que esta opción se elija, el arreglo debe volver a crearse desde cero, eliminando los datos que pudiese
contener anteriormente. NO GENERE ESTE ARREGLO DIRECTAMENTE EN LA OPCIÓN 1, AL MISMO TIEMPO QUE GRABA EL ARCHIVO.
 DEBE RESOLVER ESTE PEDIDO CON UNA OPCIÓN SEPARADA EN EL MENÚ DE OPCIONES.

4. Muestre el arreglo generado en el punto anterior, a razón de un registro por línea en la pantalla.

5. Determine si existe en el arreglo un programa en el que el nombre del entrenador coincida con el valor nom que
se carga por teclado. Si existe, detenga la búsqueda al primero que encuentre y muestre todos sus datos. Si no existe,
 cargue por teclado (o genere en forma aleatoria) un registro nuevo con los datos del programa, asigne el nombre nom del
  entrenador en el campo correspondiente, y agregue en el arreglo el nuevo registro, manteniendo el orden por clave de
  identificación.

6. Determine si existe en el arreglo un programa en que la clave de identificacion sea igual a la pasada por teclado.

7. Determine la cantidad acumulada de deportistas  que estan registrados para cada uno de los posibles deportes por
cada nivel de entrenamiento posible, muestre solo los resultados mayores a n
'''

from random import *
from classProgramaEntrenamiento import *
import os
import pickle


def entre(li, ls, msj='Ingrese un numero: '):
    n = int(input(msj))
    while n < li or n > ls:
        print(f'ERROR, el numero debe estar entre {li}, y {ls}, vuelva a intentarlo...')
        n = int(input(msj))
    return n


def mayorque(li, msj='Ingrese un numero: '):
    n = int(input(msj))
    while n < li:
        print(f'ERROR, el numero debe ser mayor a {li}, intente de vuelta...')
        n = int(input(msj))
    return n
    

def menu():
    print('BIENVENIDO AL MENU DE OPCIONES...')
    print('1) Generar un archivo binario. ')
    print('2) Muestre el archivo generado.')
    print('3) Genere un arreglo de registros con todos los programas del archivo cuya cantidad de deportistas registrados sea diferente de cero..')
    print('4) Muestre el arreglo generado en el punto anterior.')
    print('5) Determine si existe en el arreglo un programa con cierto entrenador.')
    print('6) Determine si existe en el arreglo un programa segun ID.')
    print('7) Salir del programa.')
    print('8) Salir del programa.')
    print('9) Salir del programa.')
    op = entre(1, 9, 'Elija su opcion: ')
    print()
    return op


def cargarArchivo(n, ruta):
    archivo = open(ruta, 'ab')
    for i in range(n):
        programa = Programa.generarPrograma(self=Programa)
        pickle.dump(programa, archivo)
    archivo.close()


def leerArchivo(ruta):
    if not os.path.exists(ruta):
        print('ERROR, esa ruta no existe.')
        return
    archivo = open(ruta, 'rb')
    tamanio = os.path.getsize(ruta)
    cont = 0
    while archivo.tell() < tamanio:
        programa = pickle.load(archivo)
        print(programa)
        cont += 1
    print('Se mostraron, ', cont,' programas de entrenamiento.')
    archivo.close()


def addInOrder(lista, programa):
    n = len(lista)
    izq, der = 0, n - 1
    pos = n
    while izq <= der:
        c = (izq + der) // 2
        if programa.claveID == lista[c].claveID:
            pos = n
            break
        elif programa.claveID > lista[c].claveID:
            izq = c + 1
        elif programa.claveID < lista[c].claveID:
            der = c - 1
    if izq > der:
        pos = der
    lista[pos:pos] = [programa]


def cargarArreglo(ruta):
    if not os.path.exists(ruta):
        print('ERROR, esa ruta no existe.')
        return
    archivo = open(ruta, 'rb')
    tamanio = os.path.getsize(ruta)
    l = []
    while archivo.tell() < tamanio:
        programa = pickle.load(archivo)
        if programa.cantDeportistas != 0:
            addInOrder(l, programa)
    archivo.close()
    return l


def mostrarArreglo(entrenamientos):
    for entrenamiento in entrenamientos:
        print(entrenamiento)


def existeEntrenador(nom, programas):
    for entrenamiento in programas:
        if entrenamiento.nomEntrenador.lower() == nom.lower():
            return entrenamiento
    return None

def existeProgramasegunID(id, programas):
    n = len(programas)
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if programas[c].claveID == id:
            return c
        elif programas[c].claveID > id:
            der = c - 1
        elif programas[c].claveID < id:
            izq = c + 1
    if izq > der:
        return izq
    return -1


def acumularDeportistas(programas):
    #   Cada posible deporte por cada posible nivel de entrenamiento
    #   Filas:    Deportes
    #   Columnas: Niveles de entrenamiento
    cantColumnas = 10  # Va del 0 al 9
    cantFilas = 50     # Va del 1 al 50
    m = []
    for i in range(cantFilas):
        fila = []
        for j in range(cantColumnas):
            fila.append(0)
        m.append(fila)

    for programa in programas:
        m[programa.deporte - 1][programa.nivel] += programa.cantDeportistas
    return m


def mostrarmatriz(ma, n):
    for i in range(len(ma)):
        for j in range(len(ma[0])):
            if ma[i][j] < n:
                continue
            else:
                dep = Programa.deporteToString(i)
                niv = Programa.nivelToString(j)
                print(f'Deporte: {dep} y Nivel: {niv} tienen {ma[i][j]} deportistas')


def principal():
    op = -1
    programas = []
    ruta = 'programa.dat'
    while op != 0:
        op = menu()

        if op == 1:
            n = mayorque(0, 'Ingrese la cantidad de programas a añadir en el archivo: ')
            cargarArchivo(n, ruta)
            print('Carga exitosa!!!')
            print()

        elif programas == None:
            print()
            print('ERROR, primero debe generar el/los entrenamiento/s, pruebe con la opcion 1...')
            continue

        if op == 2:
            leerArchivo(ruta)
            print()

        if op == 3:
            programas = cargarArreglo(ruta)
            print()

        if op == 4:
            mostrarArreglo(programas)
            print()

        if op == 5:
            nom = input('Ingrese el nombre del entrenador que desea buscar: ')
            programa = existeEntrenador(nom, programas)
            if programa is None:
                print('No se encntro tal entrenador')
                prog = Programa.generarPrograma(self=Programa)
                prog.nomEntrenador = nom
                addInOrder(programas, prog)
            else:
                print(programa)

        if op == 6:
            id = input('Ingrese el id que esta buscando: ')
            existe = existeProgramasegunID(id, programas)
            if existe == -1:
                print('No existe un programa con tal id...')
                print()
                continue
            else:
                print(programas[existe])
                print()

        if op == 7:
            ma = acumularDeportistas(programas)
            n = mayorque(0, 'Ingrese la cantidad minima de deportistas: ')
            mostrarmatriz(ma, n)

        if op == 8:
            pass

        if op == 9:
            print('Fue un gusto conocerte, adios!!')
            print('´' * 80)
            break


if __name__ == '__main__':
    principal()