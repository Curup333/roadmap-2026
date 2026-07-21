#1 es_primo devuelve True/False
def es_primo(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    return False

print(es_primo(1))


#2 function contar vocales
def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    suma_vocales = 0

    for letra in texto:
        if letra in vocales:
            suma_vocales += 1
    print(suma_vocales)

contar_vocales("Angel")

#3 function calcular_promedio
def calcular_promedio(lista_notas):
    suma = 0
    for nota in lista_notas:
        suma += nota
    return suma / len(lista_notas)

print(calcular_promedio([10, 8, 9]))

#4 function convertir_temperatura(grados, scala) que convierte entre Celsius y Fahrenheit segun el parametro de scala
def convertir_temperatura(grados, scala):
    if scala == "C":
        return grados * 9 / 5 + 32
    elif scala == "F":
        return (grados - 32) * 5 / 9
    elif scala == "":
        return "Error: Falta el parametro de scala"
    return None


print(f"Convertido a Fahrenheit: {convertir_temperatura(20, "C")}")
print(f"Convertido a Celsius: {convertir_temperatura(68, "F")}")
print(f"Error: {convertir_temperatura(20, "")}")

#5 function filtrar_pares(lista) que devuelva un NUEVA lista solo con los numeros pares, sin modificar la original.
def filtrar_pares(lista):
    lista_pares = []

    for numero in lista:
        if numero % 2 == 0:
            lista_pares.append(numero)
    return lista_pares

print(filtrar_pares([1, 2, 3, 4, 5, 6]))