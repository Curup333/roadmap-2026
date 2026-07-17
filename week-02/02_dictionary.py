
persona = {"nombre": "Ana", "edad": 25, "activo": True}
print(persona["nombre"])
print(persona.get("telefono", "No registrado")) # evalua si existe el elemento, si no existe devuelve el valor por defecto

# Agregar elementos
persona["edad"] = 26
persona["ciudad"] = "Bogota"
print(persona)

# Eliminar elementos
del persona["activo"]
print(persona)

persona.pop("edad")
print(persona)

# Recorrer un diccionario
for key, value in persona.items():
    print(f"{key}: {value}")

# Diccionarios anidados: lista de diccionarios

estudiantes = [{"nombre": "Ana", "nota": 20}, {"nombre": "Juan", "nota": 15}]

for estudiante in estudiantes:
    print(estudiante["nombre"])


