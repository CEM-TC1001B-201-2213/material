
lista = ["Ana", "Pablo", "Juan", "María", "Marta"]

nombre = input("Introduce el nombre del alumno al buscar: ")
for i in lista:
    if nombre == i:
        print("Alumno encontrado.")
        break # Termina el ciclo en este punto
else: # Sólo se ejecuta si se completó el ciclo (no pasó por un break)
    print("Alumno no encontrado.")
