import baraja

class Baraja():
    
    def __init__(self, palos, numeros):
        self.palos = palos # así indicamos que la variable palos pasará a ser un atributo local
        self.numeros = numeros
        self.mazacote = baraja.crearBaraja(palos, numeros)

    def barajar(self):
        baraja.barajar(self.mazacote) # la función barajar del módulo baraja.py ahora está dentro de esta clase.