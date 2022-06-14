'''
Programa que muestra una competencia entre Atletas
'''

from random import randint
from atleta import Atleta

competidores = [Atleta("") for i in range(10)]
for i in range(10):
    competidores[i].bautizar(f"Atleta {i}")
hayGanador = False
while (not hayGanador):
    for i in range (10):
        x = randint(1, 6)
        y = randint(1, 6)
        competidores[i].irHasta(x, y)
        competidores[i].mostrar()
        if competidores[i].distancia >= 100:
            print(f"Ha ganado: {competidores[i].nombre}")
            hayGanador=True
            break
