# i -> iterador
# range(número) -> Genera una secuencia numérica desde 0 hasta antes de número
# avanzando de 1 en 1
for i in range(5):
    print(f"Valor de i: {i}")

print("----------------------------")

# range(inicio, final) -> Genera una secuencia numérica desde inicio hasta
# antes de final avanzando de 1 en 1
for i in range(3,8):
    print(f"Valor de i: {i}")
    
print("----------------------------")

# range(inicio, final, paso) -> Genera una secuencia numérica desde inicio hasta
# antes de final avanzando de paso en paso
for i in range(3,10,2):
    print(f"Valor de i: {i}")
    
print("----------------------------")

for i in range(10,5,-1):
    print(f"Valor de i: {i}")
    
print("----------------------------")

texto = "hola mundo"
# La variable i recorre el contenido de texto tomando el valor de cada uno de
# sus caracteres
for i in texto:
    print(f"Valor de i: {i}")

print("----------------------------")

lista = [1,4.6,"hola",True,[5,7]]
# La variable i recorre el contenido de lista tomando el valor de cada uno
# de sus elementos
for i in lista:
    print(f"Valor de i: {i}")