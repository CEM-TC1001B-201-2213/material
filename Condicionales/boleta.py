numero_udfs = int(input("Indica el número de unidades de formación que cursaste: "))

promedio = 0
for i in range(numero_udfs):
    udf = float(input(f"Introduce la calificación de tu udf{i+1}: "))
    promedio = promedio + udf

promedio = promedio / numero_udfs

print(f"El promedio de tu semestre fue de: {promedio:,.2f}.")