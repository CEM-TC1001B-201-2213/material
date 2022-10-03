
numero = int(input("Ingrese su número: "))
pares = 0
nones = 0
for i in range(1,numero+1):
    if i % 2 == 0:
        pares = pares + i
    else:
        nones = nones + i

print(f"Pares: {pares}")
print(f"Nones: {nones}")