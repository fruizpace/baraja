import random

def crearBaraja():
    palos = ['o', 'c', 'e', 'b']
    numeros = ['A', '2', '3','4','5','6','7','S','C','R']
    baraja = [] # lista vacía y lo ponemos como una variable local (si lo pusiéramos fuera de la función sería una variable global)
    
    for palo in palos: # primera iteración
        for numero in numeros: # segunda iteración
            baraja.append(numero+palo)
    return baraja    

miB = crearBaraja()
#print(miB)
#print(miB[2])


def barajando(miBaraja):
    newBaraja = []
    while len(newBaraja) < len(miBaraja):
        item = random.randint(0, len(miBaraja)-1)
        carta = miBaraja[item]
        if carta in newBaraja:
            item = random.randint(0, len(miBaraja)-1) 
        else:
            newBaraja.append(carta)
                
    return newBaraja
'''
print(barajando(miB))

print(miB[:4])
jugadores = []
jugadores = [[],[]] # lista de listas vacías
jugadores.append([]) # añadimos una lista vacía
jugadores[1].append('a') # metemos un elemento en la lista 1
jugadores[0].append(miB[0])
print(jugadores)
miB
jugadores[0].append(miB.pop(0)) # con la función POP, coge el elemento de la lista y lo EXTRAE. deja de estar en la lista miB.
'''


## si queremos repatir la baraja entre jugadores:
mazacote = crearBaraja()
print(mazacote)
jugadores = []
num_jugadores = 3
num_cartas = 5

for i in range(num_jugadores): # crea tantas listas vacías como jugadores
    jugadores.append([])

for carta in range(num_cartas):
    for jugador in range(num_jugadores):
        jugadores[jugador].append(mazacote.pop(0))
print(jugadores)
print(mazacote)

