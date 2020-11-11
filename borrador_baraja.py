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
            item = random.randint(1, len(miBaraja)-1)
        else:
            newBaraja.append(carta)
    return newBaraja

print(barajando(miB))