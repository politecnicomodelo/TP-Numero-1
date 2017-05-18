from datetime import date
class Persona(object):

    Nombre=" "

    Apellido=" "

    FechaN=None

    DNI=None

    def setNombre(self, n):
        self.Nombre=n

    def setApellido(self, n):
        self.Apellido=n

    def setFechaN(self, Anio, Mes, Dia):
        self.FechaN=date(int(Anio), int(Mes), int(Dia))

    def setDNI(self, n):
        self.DNI=n