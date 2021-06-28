# Seacrh Tree in Python
#       - Mnstre @ June, 2021
from typing import Collection
from graphManager import GraphManager
from vertex import VertexFactory
from edge import EdgeFactory
import collections

gM = GraphManager()
vFactory = VertexFactory()
eFactory = EdgeFactory()

file = "path"
gM.loadGraph(file, vFactory, eFactory)