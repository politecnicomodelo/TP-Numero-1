from .Personas import Persona
class Tripulacion(Persona):

    def __init__(self):
        self.ListaAviones=[]

    def addAviones(self, n):
        self.ListaAviones.append(n)