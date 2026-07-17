## Tuplas
# Las tuplas son listas que no se pueden modificar
coordenada = (10, 20)
print(coordenada)

# coordenada[0] = 5
# print(coordenada)

# Unpacking de tuplas
x, y = coordenada

for nombre, edad in [("Ana", 25), ("Juan", 30)]:
    print(nombre, edad)