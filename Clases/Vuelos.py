from datetime import date
from .Pilotos import Pilotos
from .ServicioAbordo import ServicioAbordo
from .Aviones import Aviones
from .Pasajeros import Pasajeros
class Vuelo(object):

    Avion=None

    ListaPersonas=[]

    Fecha=None

    Hora=None

    Origen=None

    Destino=None

    def setAvion(self, n):
        self.Avion=n

    def setPersona(self, n):
        self.ListaPersonas.append(n)

    def setFecha(self, Anio, Mes, Dia):
        self.Fecha=date(int(Anio), int(Mes), int(Dia))

    def setHora(self, n):
        self.Hora=n

    def serOrigen(self, n):
        self.Origen=n

    def setDestino(self, n):
        self.Destino=n