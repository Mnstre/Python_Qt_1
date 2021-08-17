#############################
counter = 0
file = open("graph.txt", "r")

lista = []

for linea in file:
    dato = ""
    for letra in linea:
        if letra.isdigit():
            dato = dato + letra
        else:
            lista = lista + [int(dato)]
            dato = ''