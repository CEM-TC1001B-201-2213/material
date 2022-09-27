import random

opcion = int(input("Escribe 1) para menor a 7, 2) para igual a 7 y 3) para mayor a 7: "))

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)

suma = dado1 + dado2

print(f"El dado 1 cayó: {dado1}")
print(f"El dado 2 cayó: {dado2}")
print(f"La suma de los dados fue de: {suma}")

if suma < 7 and opcion == 1:
    print("Felicidades, ganaste.")
elif suma == 7 and opcion == 2:
    print("Felicidades, ganaste.")
elif suma > 7 and opcion == 3:
    print("Felicidades, ganaste.")
else:
    print("Lo siento, perdiste.")