
cuenta = 0
precio = 0
while precio >= 0:
    # cuenta = cuenta + precio
    cuenta += precio
    precio = float(input("Introduce el precio de tu producto: "))

print(f"El total a pagar es: ${cuenta:,.2f}")