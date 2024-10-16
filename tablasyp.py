#Vicente Y. Lopez V. - 240010
#tablas de multiplicar



print("Primera Parte: Tablas de multiplicar del 1 al 3\n")
for i in range(1, 4):  # Números 1, 2 y 3
    print(f"Tabla de multiplicar del {i}:")
    for j in range(1, 11):  
        print(f"{i} x {j} = {i * j}")
    print()  

# Segunda parte: Solo imprimir los resultados pares
print("Segunda Parte: Tablas de multiplicar con solo resultados pares\n")
for i in range(1, 4):  # Números 1, 2 y 3
    print(f"Tabla de multiplicar del {i} (Solo resultados pares):")
    for j in range(1, 11):  
        resultado = i * j
        if resultado % 2 == 0:  
            print(f"{i} x {j} = {resultado}")
    print()  


