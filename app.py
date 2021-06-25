# Seacrh Tree in Python
#       - Mnstre @ June, 2021
from graphManager import GraphManager
from vertex import VertexFactory
from edge import EdgeFactory

gM = GraphManager()
vFactory = VertexFactory()
eFactory = EdgeFactory()
#for iterator from listaDeVectores
gM.loadGraph(vFactory, eFactory)