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

newBaraja = []
#for item in range(0, 40):




#print(miB[item])
#print(newBaraja)
while len(newBaraja) < len(miB):
    item = random.randint(0, len(miB-1))
    carta = miB[item]
        if carta in newBaraja:
            item = random.randint(1, 40)
        else:
            newBaraja.append(carta)


print(newBaraja)

# Using randrange() to generate numbers from 0-100
print ("Random number from 0-100 is : ",end="")
print (random.randrange(100))