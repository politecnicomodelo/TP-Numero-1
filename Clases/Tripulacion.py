from .Personas import Persona
class Tripulacion(Persona):

    ModelosAvion=None

    def setModelosAvion(self, n):
        self.ModelosAvion=n