import pandas as pd
import PySimpleGUI as sg

def crearVentanaDatos():
    datos = pd.read_csv("Bienes Muebles.csv")
    # Obtener el nombre de las columnas y las guarda en una lista
    columnas = datos.columns.tolist()
    # Obtenemos los datos y los guardamos como lista
    valores = datos.head(10).values.tolist()
    suma = datos["valor_en_inventario"].sum()
    
    layout = [
        [sg.Text("Tabla de Bienes Muebles")],
        [sg.Table(headings=columnas, values=valores)],
        [sg.Text(f"Total: ${suma:,.2f}")]
        ]
    return sg.Window("Bienes Muebles", layout, finalize=True)

ventanaDatos = crearVentanaDatos()

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WINDOW_CLOSED:
        window.close()
        break