
numero = int(input("Indique hasta qué número quiere hacer su sumatoria: "))

suma = 0
for i in range(1,numero+1):
    suma = suma + i

print(f"El resultado de sumar de 1 hasta {numero} es: {suma}")