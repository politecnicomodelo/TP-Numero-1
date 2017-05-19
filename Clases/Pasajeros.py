from .Personas import Persona
class Pasajero(Persona):

    VIP=None

    Necesidades=None

    def setVIP(self, n):
        self.VIP=n

    def setNecesidades(self, n):
        self.Necesidades=n