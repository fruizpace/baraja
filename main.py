'''
import baraja
palos = ['o', 'c', 'e', 'b']
numeros = ['A', '2', '3','4','5','6','7','S','C','R']
ordenada = baraja.crearBaraja(palos, numeros) # creamos la baraja con la función 1 en baraja.py
print("ordenada: ", ordenada)

desordenada = baraja.crearBaraja(palos, numeros)
baraja.barajar(desordenada)
print("desordenada: ", desordenada)
'''

import barajaC

palos = ['o', 'c', 'e', 'b']
numeros = ['A', '2', '3','4','5','6','7','S','C','R']

miBaraja = barajaC.Baraja(palos, numeros) # creamos la clase Baraja que está en el módulo barajaC

print(miBaraja.mazacote) # me da una baraja mezclada pq he llamado a la función barajar

miBaraja.barajar() # me da una baraja sin mezclar
print(miBaraja.mazacote)

# quiero el elemento 2 de miBaraja:
miBaraja.mazacote[2] # como miBaraja es un objeto, para acceder al elemento 2 tengo que poner primero el atributo que contiene la cartas, o sea mazacote.
