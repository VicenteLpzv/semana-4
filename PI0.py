#Vicente Y. Lopez V. - 240010


p = 0
im = 0
c = 0

print ("Este programa le permite contar pares, impares y ceros ingresados")

for i in range(10):
    n = int(input(f"Ingresa cualquier numero {i + 1}: "))
  
    if n == 0:
        c += 1
    elif n %2 == 0:
        p += 1
    else:
        im += 1
   
        
print (f"los pares son {p} números")
print (f"los impares son {im} números")
print (f"los ceros son {c} números")