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

miBaraja = barajaC.Baraja(palos, numeros) # creamos la clase

print(miBaraja.mazacote) # me da una baraja mezclada

miBaraja.barajar() 
print(miBaraja.mazacote)