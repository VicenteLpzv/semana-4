#Vicente Y. Lopez V. - 240010
#programa que registra las temperaturas de los ultimos 7 dias

# Lista para almacenar las temperaturas ingresadas
temp = []
days = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

# Pedir la temperatura para cada día
for dia in days:
    t = float(input(f"Ingrese la temperatura para el día {dia}: "))
    temp.append(t)  # Guardamos cada temperatura en la lista

# Verificar que las temperaturas se guardaron correctamente
print("\nTemperaturas registradas:")
for dia, t in zip(days, temp):
    print(f"{dia}: {t}°C")


promedio = sum(temp) / len(temp)


maxima = max(temp)
minima = min(temp)


print("\nEstadísticas de Temperaturas:")
print(f"Temperatura promedio: {promedio:.2f}°C")
print(f"Temperatura más alta: {maxima}°C")
print(f"Temperatura más baja: {minima}°C")
