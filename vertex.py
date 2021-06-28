#Clase Vertex
#   - Constructor and functions
class Vertex:
    def __init__(self, key):
        self.__id = key
        self.x = None
        self.y = None

    def getId(self):
        return self.__id

class VertexFactory(Vertex):
    def createVertex(id):
        return Vertex(id)