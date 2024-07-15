'''
De cada Programa, se tiene una clave de identificación (una cadena que puede tener dígitos y caracteres), el nombre del
 entrenador a cargo de ese programa, la descripción del contenido de ese programa (una cadena con un texto terminado en
punto y con palabras separadas por un blanco. Por ejemplo: "Entrenamiento intensivo en judo para varones de menos de 70
kilos.", etc.), la cantidad de deportistas registrados para ese programa (puede valer cero), un número entre 1 y 50 que
indica el deporte para ese programa (por ejemplo: 1: fútbol, 2: basquet, etc.), y otro número pero entre 0 y 9 para
indicar el nivel de entrenamiento ofrecido en ese programa (por ejemplo: 0: de alta competencia, 1: de recuperación, 2:
de competencia inicial, etc.).
'''


from random import *


class Programa():
    def __init__(self, claveID, nomEntrenador, desc, cantDeportistas, deporte, nivel):
        self.claveID = claveID
        self.nomEntrenador = nomEntrenador
        self.desc = desc
        self.cantDeportistas = cantDeportistas
        self.deporte = deporte
        self.nivel = nivel


    def deporteToString(nDep):
        return 'Deporte' + str(nDep)


    def nivelToString(nNivel):
        return 'Nivel' + str(nNivel)


    def __str__(self):
        deporte = Programa.deporteToString(self.deporte)
        nivel = Programa.nivelToString(self.nivel)
        xd = f'Clave de ID: {self.claveID}' \
             f'  Nombre del entrenador: {self.nomEntrenador} ' \
             f'  Descripcion: {self.desc}' \
             f'  Cantidad de deportistas: {self.cantDeportistas}' \
             f'  Deporte: {deporte}' \
             f'  Nivel de entrenamiento: {nivel}'
        return xd


    def generarPrograma(self):
        id = chr(randint(65, 90)) + str(randint(0, 100)) + chr(randint(65, 90))
        nE = choice(('Martin', 'Ivo', 'Fede', 'Lautaro', 'Pia', 'Ivan', 'Santiago', 'Nico', 'Leandro', 'Agustina',
                     'Emilia', 'Andrea', 'Javier', 'Patricia', 'Esmeralda', 'Estrella', 'Guille', 'Orne', 'Vale',
                     'Fausto'))
        desc = chr(randint(65, 90)) + chr(randint(65, 90)) + chr(randint(65, 90)) + chr(randint(65, 90))
        cantD = randint(0, 20)
        deporte = randint(1, 50)
        nivel = randint(0, 9)
        return Programa(id, nE, desc, cantD, deporte, nivel)


