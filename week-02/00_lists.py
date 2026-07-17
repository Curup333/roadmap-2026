fruits = ['water melon', 'apple', 'banana', 'orange']
print(fruits[1]) # Se accede por indice empezando en 0
print(fruits[0:2]) # El slicing te da los dos primeros elementos

# Agregar elementos
fruits.append('Kiwi')
print(fruits)

# Inserta un elemento en una posicion especifica
fruits.insert(1, 'mango')
print(fruits)

# Eliminar por valor
fruits.remove('orange')
print(fruits)

# elimina y devuelve el ultimo elemento
fruits.pop()
print(fruits)

# Contar elementos
print(len(fruits))

# Ordenar alfabeticamente
print(sorted(fruits))

fruits.sort()
print(fruits)

# Verificar si un elemento esta en la lista
print(f"Manzana se encuentra en frutas: {'apple' in fruits}")

# Invertir la lista
fruits.reverse()
print(fruits)

# Recorrer listas con for (repaso concetado con loops)

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers_list:
    if number % 2 == 0:
        print(number)



