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
# crearlo como una función
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