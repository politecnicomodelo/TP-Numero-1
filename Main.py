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
            unPasajero.setFechaN(int(Fecha[2]), int(Fecha[1]), int(Fecha[0]))
            unPasajero.setDNI(Auxiliar[4])
            unPasajero.setVIP(Auxiliar[5])
            unPasajero.setNecesidades(Auxiliar[6])

            ListaPersonas2.append(unPasajero)

        if Auxiliar[0]=="Piloto":
            unPiloto=Piloto()
            unPiloto.setNombre(Auxiliar[1])
            unPiloto.setApellido(Auxiliar[2])
            Fecha=Auxiliar[3].split("-")
            unPiloto.setFechaN(int(Fecha[2]), int(Fecha[1]), int(Fecha[0]))
            unPiloto.setDNI(Auxiliar[4])
            unPiloto.setModelosAvion(Auxiliar[5])

            ListaPersonas2.append(unPiloto)

        if Auxiliar[0]=="Servicio":
            unServicio=ServicioAbordo()
            unServicio.setNombre(Auxiliar[1])
            unServicio.setApellido(Auxiliar[2])
            Fecha=Auxiliar[3].split("-")
            unServicio.setFechaN(int(Fecha[2]), int(Fecha[1]), int(Fecha[0]))
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
        unAvion.setCantTripulacion(Auxiliar[2])

        ListaAviones2.append(unAvion)

    p.close()

def cargarVuelos():
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

        Fecha = Aux[1].split("-")
        unVuelo.setFecha(int(Fecha[2]), int(Fecha[1]), int(Fecha[0]))

        unVuelo.setHora(Aux[2])
        unVuelo.setOrigen(Aux[3])
        unVuelo.setDestino(Aux[4])

        Pasajeros = Aux[5].split(",")
        for pdni in Pasajeros:
            for item in ListaPersonas2:
                if item.DNI == pdni:
                    unVuelo.addPasajero(item)

        Tripulantes = Aux[6].split(",")
        for pdni in Tripulantes:
            for item in ListaPersonas2:
                if item.DNI == pdni:
                    unVuelo.addTripulantes(item)

        ListaVuelos.append(unVuelo)

    p.close()

cargarPersonas()
cargarAviones()
cargarVuelos()

while 1:
    os.system("clear")

    print("1- Nomina personas por vuelo")
    print("2- Pasajero mas joven por vuelo")
    print("3- Vuelos que no alcanzan la tripulacion minima")
    print("4- Vuelos tripulados por no autorizados")
    print("5- Tripulantes que hacen mas de un vuelo por dia")
    print("6- Personas VIP o con necesidades especiales por vuelo")
    print("7- Salir")
    print(" ")
    Eleccion=input("Elija opcion: ")


    if Eleccion == "1":
        os.system("clear")

        Contador=0
        for item in ListaVuelos:
            Contador+=1
            Auxiliar=len(item.ListaTripulantes)+len(item.ListaPasajeros)
            print("La nomina del vuelo %s es de %s" %(Contador, Auxiliar))

        input("Enter para continuar")

    if Eleccion == "2":
        ListaMenores=[]
        menor = None
        for item in ListaVuelos:
            menor=None
            for item2 in item.ListaPasajeros:
                if menor == None:
                    menor = item2

                if menor.FechaN < item2.FechaN:
                    menor = item2
            ListaMenores.append(menor)

        os.system("clear")
        NroVuelo=0
        for item in ListaMenores:
            NroVuelo+=1
            print("El pasajero mas joven del vuelo %s es %s %s" % (NroVuelo, item.Nombre, item.Apellido))
        input()

    if Eleccion == "3":
        os.system("clear")

        Auxiliar=False

        for item in ListaVuelos:
            if len(item.ListaTripulantes) < int(item.Avion.CantTripulacion):
                print("El vuelo con origen en %s y destino en %s no alcanza la cantidad minima" %(item.Origen, item.Destino))
                Auxiliar=True

        if not Auxiliar:
            print("No hay ningun vuelo al que le falten tripulantes ")

        input("Enter para continuar")

    if Eleccion == "7":
        break





