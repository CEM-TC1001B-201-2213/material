
numero = int(input("Ingrese el número sobre el que quiere calcular su factorial: "))

# Resuelto con for
factorial = 1
for i in range(numero,1,-1):
    factorial = factorial * i
print(f"El factorial de {numero} es: {factorial}")

# Resuelto con while
factorial = 1
i = numero
while i > 1:
    factorial = factorial * i
    i = i - 1
print(f"El factorial de {numero} es: {factorial}")