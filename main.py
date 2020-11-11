import baraja

ordenada = baraja.crearBaraja() # creamos la baraja con la función 1 en baraja.py
print("ordenada: ", ordenada)

desordenada = baraja.crearBaraja()
baraja.barajar(desordenada)
print("desordenada: ", desordenada)