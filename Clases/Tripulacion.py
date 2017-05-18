from .Personas import Personas
class Tripulacion(Personas):

    ModelosAvion=None

    def setModelosAvion(self, n):
        self.ModelosAvion=n