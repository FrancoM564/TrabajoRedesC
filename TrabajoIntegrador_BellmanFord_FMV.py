import math                        #Importar la libreria math para otorgar el valor infinito a los costos iniciales
from timeit import default_timer                              #Importar la libreria time para realizar mediciones de tiempo


class Router:                               
    def __init__(self,i):
        self.id=i                          
        self.vecinos=[]                                 
        self.padre = None                   
        self.costo = float('inf')          
        self.caminosycostos={}
    
    def agregarVecino(self,id_vecino,costo_vecino):            
        if [id_vecino,costo_vecino] not in self.vecinos:       
            self.vecinos.append([id_vecino,costo_vecino])

class Topologia:                           
    def __init__(self):
        self.vertices={}                    

    def agregarRouter(self,id):             
        if id not in self.vertices:         
            self.vertices[id]=Router(id)
        else:                             
            print("Ya existe este router")
    
    def agregarArista(self,id1,id2,costo):                      
        if id1 in self.vertices and id2 in self.vertices:       
            self.vertices[id1].agregarVecino(id2,costo)
            self.vertices[id2].agregarVecino(id1,costo)
        else:
            print("Uno o ambos routers no se encuentra/n")
            
    def auxImprimir(self, a):
        cad = ""
        for c in self.vertices[a].caminosycostos:
            cad+="\tDestino:"+str(c)+"\n \t Camino: "
            for x in self.vertices[a].caminosycostos.get(c)[0]:
                cad+= str(x)+" --> "
            cad+="FIN\n\t Costo: "+str(self.vertices[a].caminosycostos.get(c)[1])+"\n"
        return cad
            
    def imprimirCaminos(self,a=-1):
        b = a
        if b != -1:
            if b in self.vertices:
                print(self.auxImprimir(a))
            else:
                print("No existe dicho router")
        else:
            for v in self.vertices:
                print("Caminos para "+str(v)+"\n")
                print(self.auxImprimir(v))

    def bellmanFord(self,a):
        for v in self.vertices:
            if v != a:
                self.vertices[v].costo = float('inf')
            else:
                self.vertices[v].costo=0
            self.vertices[v].padre = None
        
        for x in range(0, len(self.vertices)):
            for actual in self.vertices:
                for vec in self.vertices[actual].vecinos:
                    if self.vertices[actual].costo + vec[1] < self.vertices[vec[0]].costo:
                        self.vertices[vec[0]].costo = self.vertices[actual].costo + vec[1]
                        self.vertices[vec[0]].padre = actual

        for actual in self.vertices:
            for vec in self.vertices[actual].vecinos:
                if self.vertices[actual].costo + vec[1] < self.vertices[vec[0]].costo:
                    return "Error"
        
        for x in self.vertices:
            if x != a:
                camino = []
                actual = x
                while actual != None:
                    camino.insert(0,actual)
                    actual = self.vertices[actual].padre
                self.vertices[a].caminosycostos[x]=[camino,self.vertices[x].costo]

    def bellmanFordAll(self):
        inicio=default_timer()
        for a in self.vertices:
            self.bellmanFord(a)
        fin=default_timer()
        print("Algoritmo ejecutado")
        print("Tiempo de ejecucion:")
        print(fin-inicio)
        
class Menu:
    def __init__(self):
        self.topo = None
    
    def iniciar(self):
        self.topo = Topologia()
        print("----\tExperimentación con algoritmo vector-distancia\t----")
        n = int(input('Ingrese número de enrutadores: '))
        while n != 0:
            self.topo.agregarRouter(input('Ingrese id de router: '))
            n -= 1
        print("Ingrese las aristas con el siguiente formato separado por espacios: id1 - id2 - costo. Escriba s para terminar")
        x=input('Ingrese arista: ')
        while x.lower() != "s":
            datos = x.split(' ')
            if len(datos) != 3:
                print("Ha ingresado datos insuficientes o extra, intente nuevamente")
                x = input('Ingrese arista o s para terminar: ')
            else:
                self.topo.agregarArista(datos[0],datos[1],int(datos[2]))
                x = input('Ingrese arista o s para terminar: ')
        print("Se ejecutara el algoritmo")
        self.topo.bellmanFordAll()
        opcion = 0
        while opcion !=3:
            print("----\tOpciones de visualización\t----")
            print("1. Mostrar todos los caminos")
            print("2. Mostrar caminos de un router hacia el resto")
            print("3. Salir")
            opcion = int(input('Elegir opcion: '))
            if opcion >= 1 and opcion <= 3:
                if opcion == 1:
                    self.topo.imprimirCaminos()
                elif opcion == 2:
                    e = input('Seleccione el nodo: ')
                    self.topo.imprimirCaminos(e)
                else:
                    print("Salida del programa :3")
            else:
                print("Opcion invalida, intente nuevamente")
                
                    

class main:
    '''m = Menu()
    m.iniciar()'''
    print("Prueba con topologia de complejidad baja")
    CompleBaja = Topologia()
    CompleBaja.agregarRouter(1)
    CompleBaja.agregarRouter(2)
    CompleBaja.agregarRouter(3)
    CompleBaja.agregarRouter(4)
    CompleBaja.agregarRouter(5)
    CompleBaja.agregarRouter(6)
    CompleBaja.agregarRouter(7)
    CompleBaja.agregarArista(1,3,80)
    CompleBaja.agregarArista(1,4,48)
    CompleBaja.agregarArista(4,7,75)
    CompleBaja.agregarArista(3,7,69)
    CompleBaja.agregarArista(7,6,40)
    CompleBaja.agregarArista(4,5,15)
    CompleBaja.agregarArista(1,2,20)
    CompleBaja.agregarArista(5,2,28)
    CompleBaja.agregarArista(2,6,19)
    CompleBaja.agregarArista(5,6,17)
    CompleBaja.bellmanFordAll()
    CompleBaja.imprimirCaminos()
    '''print("Prueba con topologia de complejidad media")
    CompleMedia = Topologia()
    CompleMedia.agregarRouter(1)
    CompleMedia.agregarRouter(2)
    CompleMedia.agregarRouter(3)
    CompleMedia.agregarRouter(4)
    CompleMedia.agregarRouter(5)
    CompleMedia.agregarRouter(6)
    CompleMedia.agregarRouter(7)
    CompleMedia.agregarRouter(8)
    CompleMedia.agregarRouter(9)
    CompleMedia.agregarRouter(10)
    CompleMedia.agregarRouter(11)
    CompleMedia.agregarArista(1,10,40)
    CompleMedia.agregarArista(9,10,20)
    CompleMedia.agregarArista(10,11,92)
    CompleMedia.agregarArista(9,5,51)
    CompleMedia.agregarArista(7,9,32)
    CompleMedia.agregarArista(1,7,72)
    CompleMedia.agregarArista(2,1,43)
    CompleMedia.agregarArista(2,8,89)
    CompleMedia.agregarArista(11,6,97)
    CompleMedia.agregarArista(3,2,23)
    CompleMedia.agregarArista(5,4,17)
    CompleMedia.agregarArista(8,4,55)
    CompleMedia.agregarArista(8,6,77)
    CompleMedia.agregarArista(3,7,50)
    CompleMedia.agregarArista(4,6,50)
    CompleMedia.agregarArista(3,5,67)
    CompleMedia.bellmanFordAll()'''


    






