
numero = int(input("Ingresa el número sobre el que quieres su tabla de multiplicar: "))

for i in range(1,11):
    mult = i * numero
    print(f"{i} x {numero} = {mult}")