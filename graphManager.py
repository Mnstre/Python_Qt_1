#Main class 'GraphManger'
#   - Constructor and functions
from vertex import VertexFactory

# 3 etapas 
#   1- nVertex
#   2- mapVertex
#   3- nEdges
#   4- mapEdges
def decrypter(file1):
    lista = []        
    etapa = 0
    for linea in file:
    for letra in linea:
        if letra.isdigit():
            dato = dato + letra
        else:
            lista = lista + [int(dato)]
            dato = ''

class GraphManager:
    def __init__(self):
        self.__nVertex = None
        self.__m_keyGen = 0
        self.__mapV = None
        self.__mapE = None

    def __createVertex(self, vFactory):
        v = vFactory.createFactory(self.__m_keyGen)
        self.__m_keyGen +=1
        return v
    
    def loadGraph(self, file, vFactory, eFactory):
        file1 = open("graph.txt", "r")

        nVertex, nEdges, mapVertex, mapEdges = decrypter(file1)

        x = None
        y = None
        ########
        #Asignar valores al Vertex
        nodo.x = x
        nodo.y = y
        ##########
        self.m_keyGen += 1
        return nodo