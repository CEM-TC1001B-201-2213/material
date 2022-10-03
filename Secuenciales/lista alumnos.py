
lista = []
nombre = input("Ingrese el nombre del alumno: ").lower().strip()
while nombre != "terminar":
    if nombre in lista:
        print("Error, el nombre ya está registrado.")
    else:
        lista.append(nombre)
    nombre = input("Ingrese el nombre del alumno: ").lower().strip()
    
lista.sort()
for i in lista:
    print(f"Alumno: {i.title()}")
    