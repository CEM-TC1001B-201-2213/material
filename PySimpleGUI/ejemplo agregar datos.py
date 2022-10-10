import pandas as pd

datos = pd.read_csv("Bienes Muebles.csv")

# "nombre columna": valor
nuevo_registro = {
    # "codigo": values["input código"],
    "codigo": 12345,
    "descripcion": "Alguna descripción",
    "valor_en_inventario": 852963,
    "moneda": "PESOS"
    }

datos = datos.append(nuevo_registro, ignore_index=True)
datos.to_csv("Bienes Muebles.csv", index=False)