import PySimpleGUI as sg

sg.theme("BrightColors")

def crearVentanaPrincipal():
    lista_vacunas = ["Pfizer", "Moderna", "AstraZeneca", "Sputnik", "Cansino"]
    lista_spinbox = ["Uno", "Dos", "Tres"]
    layout = [
        [sg.Text("Mi primer texto",
                 font="Arial 30",
                 text_color="red",
                 background_color="white"),
         sg.Text("Soy otro texto")],
        [sg.Button("Soy un botón",
                   key="botón1",
                   image_filename="eeevee.png"),
         sg.Button("Otro botón", key="botón2")],
        [sg.Text("Usuario"),
         sg.Input(key="input usuario", default_text="Usuario...")],
        [sg.Text("Contraseña"),
         sg.Input(key="input contraseña", password_char="*")],
        [sg.Text("Estado de vacunación"),
         sg.Radio("Estoy vacunado",
                  key="radio vacunación sí",
                  group_id="radio vacunación",
                  enable_events=True),
         sg.Radio("No estoy vacunado",
                  key="radio vacunación no",
                  group_id="radio vacunación",
                  default=True,
                  enable_events=True)],
        [sg.Text("Marca de la vacuna"),
         sg.Combo(lista_vacunas,
                  key="combo vacunas",
                  default_value="Pfizer",
                  disabled=True)],
        [sg.Text("Pasatiempos"),
         sg.Checkbox("Ver series", key="checkbox series"),
         sg.Checkbox("Leer libros", key="checkbox libros"),
         sg.Checkbox("Escuchar música", key="checkbox música")],
        [sg.Text("Slider"),
         sg.Slider(range=(1,10),
                   key="slider",
                   orientation="horizontal")],
        [sg.Text("Spin"),
         sg.Spin(lista_spinbox, key="spin", initial_value="Dos")],
        [sg.Image("eeevee.png")]
        ]
    return sg.Window("Mi ventana principal", layout, finalize=True)

ventanaPrincipal = crearVentanaPrincipal()

while True:
    # Revisa lo ocurrido en todas las ventanas
    # window -> Indica en qué ventana ocurrió el evento
    # event -> Indica cuál fue el evento ocurrido
    # values -> Información contenida en los elementos
    window, event, values = sg.read_all_windows()
    
    if event == sg.WINDOW_CLOSED:
        window.close()
        break
    elif event == "botón1":
        print("Click en el botón 1...")
        usuario = values["input usuario"]
        contraseña = values["input contraseña"]
        print(f"Usuario: {usuario} - Contraseña: {contraseña}")
        vacunacion_si = values["radio vacunación sí"]
        vacunacion_no = values["radio vacunación no"]
        print(f"Vacunado: {vacunacion_si} - No vacunado: {vacunacion_no}")
        marca_vacuna = values["combo vacunas"]
        print(f"Marca vacuna: {marca_vacuna}")
        check_series = values["checkbox series"]
        check_libros = values["checkbox libros"]
        check_musica = values["checkbox música"]
        print(f"Checkbox series: {check_series}")
        print(f"Checkbox libros: {check_libros}")
        print(f"Checkbox música: {check_musica}")
        slider = values["slider"]
        print(f"Slider: {slider}")
    elif event == "botón2":
        print("Dimos click en el botón 2...")
    elif event == "radio vacunación sí":
        window["combo vacunas"].update(disabled=False)
    elif event == "radio vacunación no":
        window["combo vacunas"].update(disabled=True)
    