
numero = int(input("Ingrese su número: "))

# Resuelto con for
pares = 0
nones = 0
for i in range(1,numero+1):
    if i % 2 == 0:
        pares = pares + i
    else:
        nones = nones + i

print(f"Pares: {pares}")
print(f"Nones: {nones}")

# Resuelto con while
pares = 0
nones = 0
i = 1
while i <= numero:
    if i % 2 == 0:
        pares = pares + i
    else:
        nones = nones + i
    i = i + 1

print(f"Pares: {pares}")
print(f"Nones: {nones}")