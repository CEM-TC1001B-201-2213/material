
numero = int(input("Ingresa el número sobre el que quieres su tabla de multiplicar: "))

# Resuelto con for
for i in range(1,11):
    mult = i * numero
    print(f"{i} x {numero} = {mult}")
    
# Resuelto con while
i = 1
while i <= 10:
    mult = i * numero
    print(f"{i} x {numero} = {mult}")
    i = i + 1