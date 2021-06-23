#Main class 'GraphManger'
#   - Constructor and functions
from vertex import Vertex
from edge import Edge

class GraphManager:
    def __init__(self):
        self.nVertex = None
        self.m_keyGen = 0
        #método Get Vertex
        #
        
    def addVertex(self, x, y):
        nodo = Vertex(self.m_keyGen)
        nodo.x = x
        nodo.y = y
        self.m_keyGen += 1
        return nodo