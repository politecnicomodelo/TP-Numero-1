from datetime import date
from .Pilotos import Piloto
from .ServicioAbordo import ServicioAbordo
from .Aviones import Avion
from .Pasajeros import Pasajero
class Vuelo(object):

    def __init__(self):
        self.ListaPasajeros=[]
        self.ListaTripulantes=[]

    Avion=None

    Fecha=None

    Hora=None

    Origen=None

    Destino=None

    def setAvion(self, n):
        self.Avion=n

    def addPasajero(self, n):
        self.ListaPasajeros.append(n)

    def addTripulantes(self, n):
        self.ListaTripulantes.append(n)

    def setFecha(self, Anio, Mes, Dia):
        self.Fecha=date(int(Anio), int(Mes), int(Dia))

    def setHora(self, n):
        self.Hora=n

    def setOrigen(self, n):
        self.Origen=n

    def setDestino(self, n):
        self.Destino=n