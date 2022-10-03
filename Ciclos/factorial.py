
numero = int(input("Ingrese el número sobre el que quiere calcular su factorial: "))

factorial = 1
for i in range(numero,1,-1):
    factorial = factorial * i

print(f"El factorial de {numero} es: {factorial}")