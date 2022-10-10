import pandas as pd

datos = pd.read_csv("Bienes Muebles.csv")

# Tomar las primeras n filas
print(datos.head(5))

# Tomar las últimas n filas
print(datos.tail(5))

# Si queremos una columna, necesitamos su nombre
print(datos["valor_en_inventario"])

# Obtiene la suma total de una columna
suma_total = datos["valor_en_inventario"].sum()
print(f"La suma total es: {suma_total:,.2f}")

# Obtiene el promedio de una columna
promedio = datos["valor_en_inventario"].mean()
print(f"El promedio es de: {promedio:,.2f}")

# Obtiene el máximo y el mínimo
maximo = datos["valor_en_inventario"].max()
minimo = datos["valor_en_inventario"].min()
print(f"El máximo es: {maximo:,.2f} y el mínimo es: {minimo:,.2f}")

# Desviación estándar
std = datos["valor_en_inventario"].std()
print(f"La desviación estándar es: {std:,.2f}")