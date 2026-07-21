#Definir y llamar a funciones
def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("Ana")   # Hola, Ana

#Parametros vs argumentos
def sumar(a, b):    # a y b son los PARÁMETROS (los espacios vacíos de la receta)
    return a + b

resultado = sumar(3, 5)   # 3 y 5 son los ARGUMENTOS (los ingredientes reales que metes)

#La funcion entrega un resultado
def cuadrado(numero):
    return numero ** 2

resultado = cuadrado(4)
print(resultado)   # 16


def suma_con_print(a, b):
    print(a + b)      # solo lo muestra


def suma_con_return(a, b):
    return a + b       # lo entrega para poder usarlo

x = suma_con_print(2, 3)    # x vale None, ¡no puedes usarlo!
y = suma_con_return(2, 3)   # y vale 5, sí puedes usarlo después
print(y * 10)                # 50

#Parametros con valores por defecto
def saludar(nombre="invitado"):
    print(f"Hola, {nombre}")

saludar()          # Hola, invitado   (usa el valor por defecto)
saludar("Carlos")  # Hola, Carlos     (sobreescribe el valor por defecto)


def sumar_todos(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(sumar_todos(1, 2, 3))         # 6
print(sumar_todos(5, 10, 15, 20))   # 50


def mostrar_info(**datos):
    for llave, valor in datos.items():
        print(f"{llave}: {valor}")

mostrar_info(nombre="Ana", edad=25, ciudad="Guatemala")
# nombre: Ana
# edad: 25
# ciudad: Guatemala


def registrar(nombre, *hobbies, **detalles):
    print(f"Nombre: {nombre}")
    print(f"Hobbies: {hobbies}")
    print(f"Detalles extra: {detalles}")

registrar("Luis", "fútbol", "lectura", edad=30, ciudad="Guatemala")
# Nombre: Luis
# Hobbies: ('fútbol', 'lectura')
# Detalles extra: {'edad': 30, 'ciudad': 'Guatemala'}

#Docstrings-documentar tu funcion
def area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    Parámetro:
    radio (float): el radio del círculo

    Retorna:
    float: el área calculada
    """
    return 3.1416 * radio ** 2


print(area_circulo.__doc__)  # imprime el docstring completo


def calificacion_mas_alta(lista_estudiantes):
    highest_score = lista_estudiantes[0][1]
    highest_student = lista_estudiantes[0][0]

    for student in lista_estudiantes[1:]:
        if student[1] > highest_score:
            highest_score = student[1]
            highest_student = student[0]

    return highest_student


estudiantes = [("Ana", 9), ("Juan", 8), ("Carlos", 7)]
print(calificacion_mas_alta(estudiantes))  # Ana

#Scope de variables local y global
def variable():
    ejemplo = 10
#
# print(ejemplo) : NameError: name 'ejemplo' is not defined

vacia = ""

def variable_global():
    vacia = "Hola"
    print(vacia)

variable_global()
