def calcular_imc(peso, altura):
    return round(peso / (altura ** 2), 2)

etadisticas = calcular_imc(70, 1.75)
print(f"Datos: {etadisticas}")