from .Personas import Personas
class Pasajero(Personas):

    VIP=None

    Necesidades=None

    def setVIP(self, n):
        self.VIP=n

    def setNecesidades(self, n):
        self.Necesidades=n