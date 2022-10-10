import PySimpleGUI as sg

def crearVentanaInicioSesion():
    layout = [
        [sg.Text("Usuario"),
         sg.Input(key="input usuario")],
        [sg.Text("Contraseña"),
         sg.Input(key="input contraseña", password_char="*")],
        [sg.Button("Iniciar sesión", key="botón iniciar sesión"),
         sg.Button("Registrarse", key="botón registrarse")]
        ]
    return sg.Window("Inicio de sesión", layout, finalize=True)

def crearVentanaRegistro():
    layout = [
        [sg.Text("Usuario"),
         sg.Input(key="registro input usuario")],
        [sg.Text("Correo"),
         sg.Input(key="registro input correo")],
        [sg.Text("Contraseña"),
         sg.Input(key="registro input contraseña", password_char="*")],
        [sg.Text("Repetir contraseña"),
         sg.Input(key="registro input repetir contraseña", password_char="*")],
        [sg.Button("Registrarse", key="registro botón registrarse"),
         sg.Button("Volver", key="registro botón volver")]
        ]
    return sg.Window("Registrarse", layout, finalize=True)

def crearVentanaMenuPrincipal():
    layout = [
        [sg.Text("Menú Principal")],
        [sg.Button("Salir", key="menú principal botón salir")]
        ]
    return sg.Window("Menú Principal", layout, finalize=True)

# Variables para nuestras ventanas
# Sólo la que queremos que se abra de inicio tiene
# asignada su función y las demás tienen None
ventanaInicioSesion = crearVentanaInicioSesion()
ventanaRegistro = None
ventanaMenuPrincipal = None

# Ciclo principal - Sólo uno por programa
while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WINDOW_CLOSED or event == "menú principal botón salir":
        window.close()
        break
    # Revisar:
    # En qué ventana estoy
    # Qué botón se oprimió
    # A qué ventana me dirijo
    
    # InicioSesión -> MenuPrincipal
    elif window == ventanaInicioSesion and event == "botón iniciar sesión" and ventanaMenuPrincipal is None:
        window.close()
        ventanaInicioSesion = None
        ventanaMenuPrincipal = crearVentanaMenuPrincipal()
    # InicioSesion -> Registro
    elif window == ventanaInicioSesion and event == "botón registrarse" and ventanaRegistro is None:
        window.close()
        ventanaInicioSesion = None
        ventanaRegistro = crearVentanaRegistro()
    # Registro -> MenuPrincipal
    elif window == ventanaRegistro and event == "registro botón registrarse" and ventanaMenuPrincipal is None:
        contraseña = values["registro input contraseña"]
        repetir_contraseña = values["registro input repetir contraseña"]
        if contraseña == repetir_contraseña:
            window.close()
            ventanaRegistro = None
            ventanaMenuPrincipal = crearVentanaMenuPrincipal()
        else:
            sg.Popup("Las contraseñas no coinciden", title="Error, revisar")
    # Registro -> InicioSesion (volver)
    elif window == ventanaRegistro and event == "registro botón volver" and ventanaInicioSesion is None:
        window.close()
        ventanaRegistro = None
        ventanaInicioSesion = crearVentanaInicioSesion()