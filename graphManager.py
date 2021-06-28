#Main class 'GraphManger'
#   - Constructor and functions
from vertex import VertexFactory

class GraphManager:
    def __init__(self):
        self.__nVertex = None
        self.__m_keyGen = 0
        self.__mapV = None
        self.__mapE = None
    
    def __createVertex(self, vFactory):
        v = vFactory.createFactory(self.__m_keyGen)

        self.__m_keyGen +=1
    
    def loadGraph(self, file, vFactory, eFactory):
        file1 = open("graph.txt", "r")
        self.__nVertex = file1[0]
        if self.__nVertex:
            for iterator in file1[1:self.__nVertex]:
                nodo = self.__createVertex(vFactory)
        x = None
        y = None
        ########
        #Asignar valores al Vertex
        nodo.x = x
        nodo.y = y
        ##########
        self.m_keyGen += 1
        return nodo