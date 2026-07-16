
# 1 Crea una lista de 5 tareas y marca una como completada

list_tasks = ["Tarea 1", "Tarea 2", "Tarea 3", "Tarea 4", "Tarea 5"]
list_tasks[0] = "Tarea completada"
print(list_tasks)

# 2 Dada una lista de numeros, calcula el mpromedio sin usar sum()/len() de forma directa (usa un loop)
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_numbers = 0
counter = 0

for number in numbers_list:
    sum_numbers += number
    counter += 1

average = sum_numbers / counter
print(average)

# 3 Encontrar un duplicado en una lista
list_duplicates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_duplicates.count(2))

# 4 Invertir una lista sin usar reverse() ni [::-1] (usa un loop)
list_to_invert = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_inverted = []

for number in list_to_invert:
    list_inverted.insert(0, number)
print(list_inverted)

# 5 Dada una lista de tuplas (nombre, calificacion), encontrar quien tiene la mcalificacion mas alta
list_of_students = [("Ana", 9), ("Juan", 8), ("Carlos", 7), ("Maria", 10)]
highest_score = 0
highest_student = ""

for student in list_of_students:
    if student[1] > highest_score:
        highest_score = student[1]
        highest_student = student[0]

print(highest_student)

