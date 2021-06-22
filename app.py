# Seacrh Tree in Python
#
class Nodo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Vector:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Tree:
    def __init__(self):
        self.nNodos = None

    def addNodo(self, x, y):
        nodo = Nodo(x, y)
    
