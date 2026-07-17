
#1 Contar cuantas veces aparece cada palabra en una frase usando un diccionario
frase = "Hola, mi nombre es Ana"
palabras = frase.split()
diccionario = {}

for palabra in palabras:
    if palabra in diccionario:
        diccionario[palabra] += 1
    else:
        diccionario[palabra] = 1
print(diccionario)

#2 Dada una lista de compras con posibles duplicados, obten la lista de productos unicos con un set
lista_compras = ["manzana", "pera", "manzana", "uva", "pera"]
productos_unicos = set(lista_compras)
print(productos_unicos)

#3 Modelar un inventario de tienda como diccionario (producto: cantidad) y restar stock cuando se venda algo
inventario = {"manzana": 10, "pera": 5, "uva": 15}
producto = "manzana"
cantidad = 2
inventario[producto] -= cantidad
print(inventario)

#4 Dada dos listas de nombres (asistentes al evento A y al evento B), usar sets par asaber quienes fueron a ambos eventos
lista_asistentes_evento_A = ["Ana", "Juan", "Carlos", "Maria"]
lista_asistentes_evento_B = ["Ana", "Carlos", "Maria"]
asistentes_evento_A_y_B = set(lista_asistentes_evento_A).intersection(set(lista_asistentes_evento_B))
print(asistentes_evento_A_y_B)

#5 invertir un diccionario simple (que las claves pasen a ser valores y viceversa) usando un for + items()
estudiantes = {"Ana": 20, "Juan": 15, "Carlos": 18}
estudiantes_invertidos = {}

for key, value in estudiantes.items():
    estudiantes_invertidos[value] = key
print(estudiantes_invertidos)

