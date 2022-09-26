# Recibir el precio en pesos y el tipo de cambio
# Resultado -> Precio en dólares

# Sin parámetros y sin valor de retorno
def dolares_sin_parametros_y_sin_valor_de_retorno():
    precio_pesos = float(input("Indica el precio en pesos: "))
    tipo_cambio = float(input("Indica el tipo de cambio: "))
    precio_dolares = precio_pesos / tipo_cambio
    print(f"El precio en dólares es: ${precio_dolares:,.2f}")
    
# Con parámetros y sin valor de retorno
def dolares_con_parametros_y_sin_valor_de_retorno(precio_pesos, tipo_cambio):
    precio_dolares = precio_pesos / tipo_cambio
    print(f"El precio en dólares es: ${precio_dolares:,.2f}")

# Con parámetros y con valor de retorno
def dolares_con_parametros_y_con_valor_de_retorno(precio_pesos, tipo_cambio):
    precio_dolares = precio_pesos / tipo_cambio
    return precio_dolares

# dolares_sin_parametros_y_sin_valor_de_retorno()

# precio_pesos = float(input("Indica el precio en pesos: "))
# tipo_cambio = float(input("Indica el tipo de cambio: "))
# dolares_con_parametros_y_sin_valor_de_retorno(precio_pesos, tipo_cambio)

resultado = dolares_con_parametros_y_con_valor_de_retorno(520, 21.3)
print(f"El precio en dólares es: ${resultado:,.2f}")