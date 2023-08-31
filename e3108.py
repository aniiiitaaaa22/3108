import datetime
class Paciente:
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""
        self.__visitas = {}

    def verNombre(self):
        return self.__nombre
    def vercedula(self):
        return self.__cedula
    def vergenero(self):
        return self.__genero
    def vervisitas(self):
        return self.__visitas

    def asignarNombre(self,n):
        self.__nombre=n
    def asignarcedula(self,c):
        self.__cedula=c
    def asignargenero(self,g):
        self.__genero=g
    def asignarvisitas(self,v):
        self.__visitas=v 
class visita:
    def __init__(self):
        self.__fecha = " "
        self.__registro = " "
        self.__notas = " "
        self.__indices = object()
    
    def verfecha(self):
        return self.__fecha
    def verregistro(self):
        return self.__registro
    def vernotas(self):
        return self.__notas
    def verindices(self):
        return self.__indices
    
    def asignarfecha(self,f):
        self.__fecha = f
    def asignarregistro(self,r):
        self.__registro = r
    def asignarnotas(self,no):
        self.__notas = no
    def asignarindices(self,i):
        self.__indices = i

        



    




        
