# Equivale a for i in range(5)
i = 0 # Inicio
while i < 5: # Final -> Condición de paro
    print(f"Valor de i: {i}")
    i = i + 1 # Paso -> Cómo voy avanzando para llegar a mi condición de paro

print("-------------------")

# Equivale a for i in range(3,8)
i = 3
while i < 8:
    print(f"Valor de i: {i}")
    i = i + 1

print("-------------------")

i = 10
while i >= 1:
    print(f"Valor de i: {i}")
    i = i - 1
    
print("-------------------")

# Equivale a for i in texto
texto = "hola mundo"
i = 0
while i < len(texto):
    print(f"Valor de i: {i} y el valor de texto[{i}]: {texto[i]}")
    i = i + 1
    
print("-------------------")

# Equivale a for i in lista
lista = [7, 5.5, "hola", True, [1,2]]
i = 0
while i < len(lista):
    print(f"Valor de i: {i} y el valor de lista[{i}]: {lista[i]}")
    i = i + 1
    
print("-------------------")

pregunta = int(input("¿Deseas terminar? 1)Sí, 2)No: "))
while pregunta != 1:
    print("Repitiendo...")
    pregunta = int(input("¿Deseas terminar? 1)Sí, 2)No: "))