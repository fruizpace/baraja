import random

'''
palos = ['o', 'c', 'e', 'b']
numeros = ['A', '2', '3','4','5','6','7','S','C','R']
baraja = []
for palo in palos: # primera iteración
    for numero in numeros: # segunda iteración
        baraja.append(numero+palo) # añade la concatenación a la lista vacía

print(baraja)
print(len(baraja))
'''
# FUNCIÓN 1: crear una baraja
def crearBaraja():
    palos = ['o', 'c', 'e', 'b']
    numeros = ['A', '2', '3','4','5','6','7','S','C','R']
    baraja = [] # lista vacía y lo ponemos como una variable local (si lo pusiéramos fuera de la función sería una variable global)
    
    for palo in palos: # primera iteración
        for numero in numeros: # segunda iteración
            baraja.append(numero+palo)
    return baraja    

#miB = crearBaraja()
#print(miB)

# FUNCIÓN 2: intercambiar el contenido de dos string
def intercambio(p1, p2):
    aux = p1
    p1 = p2
    p2 = aux
    return p1, p2

#print(intercambio('Hola', 'Adios'))

# FUNCIÓN 3: mezclar las cartas de una baraja (lista)
def barajar(lista_de_naipes):
    for i in range(len(lista_de_naipes)): # va por la posición de cada carta
        nueva_pos = random.randrange(len(lista_de_naipes)) # similar a funcion randint
        #intercambio de cartas, técnica del vaso vacío:
        aux = lista_de_naipes[nueva_pos]
        lista_de_naipes[nueva_pos] = lista_de_naipes[i]
        lista_de_naipes[i] = aux
    return lista_de_naipes

#print(barajar(miB))