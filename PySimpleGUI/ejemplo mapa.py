import PySimpleGUI as sg
import webbrowser

def crearVentana():
    layout = [
        [sg.Button("Mapa", key="botón mapa")],
        [sg.Button("Video", key="botón video")],
        [sg.Button("Podcast", key="botón podcast")]
        ]
    return sg.Window("Mi actividad", layout, finalize=True)

ventana = crearVentana()

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WINDOW_CLOSED:
        window.close()
        break
    elif event == "botón mapa":
        webbrowser.open("https://www.google.com/maps/d/edit?mid=1n4BC9a9NIIMqLeEPXZE-9B3g1S943tE&usp=sharing")
    elif event == "botón video":
        webbrowser.open("https://www.youtube.com/watch?v=21X5lGlDOfg")
    