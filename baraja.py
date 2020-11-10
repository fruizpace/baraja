palos = ['o', 'c', 'e', 'b']
numeros = ['A', '2', '3','4','5','6','7','S','C','R']
baraja = [] # lista vacía
'''
for palo in palos: # primera iteración
    for numero in numeros: # segunda iteración
        baraja.append(numero+palo) # añade la concatenación a la lista vacía

print(baraja)
print(len(baraja))
'''
  
# crearlo como una función
def crearBaraja(l1, l2):
    for palo in l1: # primera iteración
        for numero in l2: # segunda iteración
            baraja.append(numero+palo)
    return print(baraja)    

crearBaraja(palos, numeros)
