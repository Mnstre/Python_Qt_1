# Seacrh Tree in Python
#       - Mnstre @ June, 2021
from graphManager import GraphManager

if __name__ == '__main__':
    gM = GraphManager()
    file = open('graph.txt', 'r')
    Lines = file.readlines()

    cBlock = 0
    cLines = 0
    for line in Lines:
        print("{:d}. {d}")