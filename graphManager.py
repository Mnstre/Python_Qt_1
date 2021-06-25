#Main class 'GraphManger'
#   - Constructor and functions
import vertex
import edge

class GraphManager:
    def __init__(self):
        self.nVertex = None
        self.m_keyGen = 0
        self.mapV = None
    
    def loadGraph(self, vFactory, eFactory):
        nodo = self.__createVertex(vFactory)
        #Funcion: Busqueda en el archivo
        x = None
        y = None
        ########
        #Asignar valores al Vertex
        nodo.x = x
        nodo.y = y
        ##########
        self.m_keyGen += 1
        return nodo
    
    def __createVertex(vFactory):
        v = vFactory.createVertex()