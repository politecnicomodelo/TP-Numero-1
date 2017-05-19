import os
from Clases.Aviones import Avion
from Clases.Pilotos import Piloto
from Clases.Pasajeros import Pasajero
from Clases.ServicioAbordo import ServicioAbordo
from Clases.Vuelos import Vuelo

ListaPersonas2=[]
ListaVuelos=[]
ListaAviones2=[]

def cargarPersonas():

    p=open("personas.dat", "r")
    for line in p:

        if line == "":
            break

        Auxiliar=line.split("|")

        if Auxiliar[0]=="Pasajero":
            unPasajero=Pasajero()
            unPasajero.setNombre(Auxiliar[1])
            unPasajero.setApellido(Auxiliar[2])
            Fecha=Auxiliar[3].split("-")
            unPasajero.setFechaN(int(Fecha[0]), int(Fecha[1]), int(Fecha[2]))
            unPasajero.setDNI(Auxiliar[4])
            unPasajero.setVIP(Auxiliar[5])
            unPasajero.setNecesidades(Auxiliar[6])

            ListaPersonas2.append(unPasajero)

        if Auxiliar[0]=="Piloto":
            unPiloto=Piloto()
            unPiloto.setNombre(Auxiliar[1])
            unPiloto.setApellido(Auxiliar[2])
            Fecha=Auxiliar[3].split("-")
            unPiloto.setFechaN(int(Fecha[0]), int(Fecha[1]), int(Fecha[2]))
            unPiloto.setDNI(Auxiliar[4])
            unPiloto.setModelosAvion(Auxiliar[5])

            ListaPersonas2.append(unPiloto)

        if Auxiliar[0]=="Servicio":
            unServicio=ServicioAbordo()
            unServicio.setNombre(Auxiliar[1])
            unServicio.setApellido(Auxiliar[2])
            Fecha=Auxiliar[3].split("-")
            unServicio.setFechaN(int(Fecha[0]), int(Fecha[1]), int(Fecha[2]))
            unServicio.setDNI(Auxiliar[4])
            unServicio.setIdiomas(Auxiliar[5])

            ListaPersonas2.append(unServicio)
    p.close()

def cargarAviones():

    p=open("aviones.dat", "r")

    for line in p:

        if line == "":
             break

        Auxiliar=line.split("|")

        unAvion=Avion()
        unAvion.setModelo(Auxiliar[0])
        unAvion.setCantPasajeros(Auxiliar[1])
        unAvion.setTripulacion(Auxiliar[2])

        ListaAviones2.append(unAvion)

    p.close()

def cargarVuelos():
    Aux=None
    p=open("vuelos.dat" ,"r")
    for line in p:
        if line == "":
            break

        Aux = line.split("|")
        unVuelo = Vuelo()

        for item in ListaAviones2:
            if item.Modelo == Aux[0]:
                unVuelo.setAvion(item)
                break

        fecha = Aux[1].split("-")
        unVuelo.setFecha(int(fecha[0]), int(fecha[1]), int(fecha[2]))
        unVuelo.setOrigen(Aux[2])
        unVuelo.setDestino(Aux[3])

        for item in ListaPersonas2:
            if item.DNI == Aux[4]:
                unVuelo.setPersona(item)

        for item in ListaPersonas2:
            if item.DNI == Aux[5]:
                unVuelo.setPersona(item)

        ListaVuelos.append(unVuelo)
    p.close()

cargarPersonas()
cargarAviones()
cargarVuelos()

while 1:
    os.system("cls")

    print("1- Nomina personas por vuelo")
    print("2- Pasajero mas joven por vuelo")
    print("3- Vuelos que no alcanzan la tripulacion minima")
    print("4- Vuelos tripulados por no autorizados")
    print("5- Tripulantes que hacen mas de un vuelo por dia")
    print("6- Personas VIP o con necesidades especiales por vuelo")
    print(" ")
    Eleccion=input("Elija opcion: ")

    if Eleccion == 2:
        ListaMenores=[]
        for item in ListaVuelos:
            menor=None
            for item2 in item.ListaPersonas:
                if menor == None:
                    menor = item2

                if menor > item2.FechaN:
                    menor = item2

                ListaMenores.append(menor)

        for item in ListaMenores:
            print("%d %d" %(ListaMenores[item].Nombre, ListaMenores[item].Apellido))





