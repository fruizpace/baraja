import baraja

class Baraja():
    
    def __init__(self, palos, numeros):
        self.palos = palos # así indicamos que la variable palos pasará a ser un atributo local
        self.numeros = numeros
        self.mazacote = baraja.crearBaraja(palos, numeros) # MI BARAJA!

    def barajar(self):
        baraja.barajar(self.mazacote) # la función barajar del módulo baraja.py ahora está dentro de esta clase.

    def repartir(self, num_jugadores, num_cartas):
        jugadores = []
        for i in range(num_jugadores): # crea tantas listas vacías como jugadores
            jugadores.append([])
        
        
        for carta in range(num_cartas):
            for jugador in range(num_jugadores):
                jugadores[jugador].append(self.mazacote.pop(0)) # ponemos 0 pq así será siempre la primera carta (como la elimina de mazacote...)
        return jugadores
