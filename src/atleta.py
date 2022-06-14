'''
Se trata de una clase que representa un Atleta que sabe su nombre, su 
posición y la distancia que ha recorrido. Se mueve por el plano cartesiano
'''
from math import sqrt

class Atleta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.posX = 0
        self.posY = 0
        self.distancia = 0
    def irHasta(self, x, y):
        tramo = sqrt((self.posX-x)**2 + (self.posY-y)**2)
        self.posX = x
        self.posY = y
        self.distancia += tramo
    def bautizar(self, nom):
        self.nombre = nom
    def mostrar(self):
        print(f"{self.nombre} ha recorrido {self.distancia}")
