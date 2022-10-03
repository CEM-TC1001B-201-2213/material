
lista = ["Ana", "Pablo", "Juan", "María", "Marta"]

nombre = input("Introduce el nombre del alumno al buscar: ")
encontrado = False
for i in lista:
    if nombre == i:
        encontrado = True
        
if encontrado == True:        
    print("Alumno encontrado.")
else:
    print("Alumno no encontrado.")