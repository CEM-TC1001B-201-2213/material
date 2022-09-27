
sueldo = float(input("Ingrese su sueldo: "))

if sueldo <= 578.52:
    limite_inferior = 0.01
    porcentaje = 0.0192
    cuota = 0
elif sueldo <= 4910.18:
    limite_inferior = 578.53
    porcentaje = 0.064
    cuota = 11.11

isr = (sueldo - limite_inferior) * porcentaje + cuota
sueldo_final = sueldo - isr
print(f"El ISR descontado fue de: ${isr:,.2f}.")
print(f"Tu sueldo después de ISR es de: ${sueldo_final:,.2f}.")