
numeros = {1, 2, 2, 3, 3, 3}
print(numeros)

# Operaciones de conjunto
a = {1, 2, 3}
b = {2, 3, 4}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

frutas = {"manzana", "pera"}

frutas.add("naranja")         # agregar UN elemento
frutas.remove("pera")         # quitar (error si no existe)
frutas.discard("kiwi")        # quitar (SIN error si no existe)
print(frutas)
print("manzana" in frutas)    # True -> verificación súper rápida de pertenencia