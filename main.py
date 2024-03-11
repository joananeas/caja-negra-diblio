import random
import subprocess
import time
import pyautogui
import webbrowser
import tkinter as tk
from tkinter import ttk
# v0.3 - Coordenates for my laptop

status = None
status_apache = None

def test_login():
    global status
    ruta_diblio = r"http://localhost/bibliodigital/login.php" # Abre una pestaña con la dirección del proyecto

    s(0.5)
    webbrowser.open(ruta_diblio) # Abrimos el navegador
    s(1)
    """
    Aquí nos encontramos en ./login.php
    """
    pyautogui.moveTo(880, 520)
    pyautogui.click() # Correo (login), click.
    s(0.5)
    pyautogui.write("joananeas") # user admin.
    s(1)
    pyautogui.moveTo(880, 550)
    pyautogui.click()
    s(1)

    pyautogui.moveTo(950, 640) # click en login
    pyautogui.click()

    """
    Aquí nos encontramos en ./index.php
    """
    status.config(text="Estado tests: Test Login completado.")
    print("[TEST] Login acabado.")


def test_buscar_libros():
    global status
    random.seed(time.time())
    ruta_diblio = r"http://localhost/bibliodigital/"
    libros = ["Viaje al centro de la Tierra", "Los tres cerditos", "Les tres bessones", "El libro de la selva"]

    webbrowser.open(ruta_diblio)
    s(0.5)

    pyautogui.moveTo(150, 250)
    pyautogui.click()  # Cerca
    s(0.5)

    r = random.choice(libros)
    pyautogui.write(r)
    s(0.5)

    pyautogui.moveTo(460, 300)
    pyautogui.click()
    status.config(text="Estado tests: Test Buscar completado.")
    print("[TEST] Buscar acabado.")


def rand_date():
    random.seed(time.time())
    d = random.randint(1, 12)  # Asegúrate de que el día esté en el rango correcto
    pyautogui.write(str(d))
    # pyautogui.press("tab")

    s(0.5)

    m = random.randint(1, 12)
    pyautogui.write(str(m))
    # pyautogui.press("tab")
    s(0.5)

    y = random.randint(2000, 2024)
    pyautogui.write(str(y))
    # pyautogui.press("tab")

    print("[MAIN] D: " + str(d) + "M: " + str(m) + "Y: " + str(y))


def test_reservar():
    global status
    random.seed(time.time())
    libros = ["Viaje al centro de la Tierra", "Los tres cerditos", "Les tres bessones", "El libro de la selva"]
    ruta_diblio = r"http://localhost/bibliodigital/reservas.php?libro="

    webbrowser.open(ruta_diblio + random.choice(libros))
    s(0.5)

    pyautogui.moveTo(160, 300)
    pyautogui.click()
    rand_date()
    s(0.5)

    pyautogui.moveTo(150, 330)
    pyautogui.click()
    rand_date()

    pyautogui.moveTo(130, 405)
    pyautogui.click() # Botón reserva
    status.config(text="Estado tests: Test Reservas completado.")
    print("[TEST] Reserva acabado.")


def start_xampp():
    global status, status_apache
    apache = r"C:\xampp\apache_start.bat"
    k = r"C:\xampp\killprocess.bat"
    mysql = r"C:\xampp\mysql_start.bat"
    # Ejecutando el script de matar procesos
    subprocess.Popen(k, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(0.5)

    # Ejecutando Apache
    subprocess.Popen(apache, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1)

    # Ejecutando MySQL
    subprocess.Popen(mysql, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1)
    print("[MAIN] Servicios Iniciados.")
    status.config(text="Estado tests: Servicios Iniciados.")
    """
    Con esto podremos runnear apache y mysql sin entrar a la GUI
    de xampp.
    """


def app():
    global status, status_apache
    print("[MAIN] App iniciada.")

    w = tk.Tk()
    w.title("Tests de caja negra - diblio")
    w.geometry("400x300")
    w.resizable(width=False, height=False)

    intro = tk.Label(w, text="Selecciona un test para ejecutarlo individualmente.")
    intro.grid(row=1, column=0, sticky='w')

    # CheckBox Variables
    login_var = tk.BooleanVar()
    buscar_var = tk.BooleanVar()
    reservar_var = tk.BooleanVar()

    # Crear CheckBoxes
    login_cb = tk.Checkbutton(w, text="Login", var=login_var)
    buscar_cb = tk.Checkbutton(w, text="Buscar", var=buscar_var)
    reservar_cb = tk.Checkbutton(w, text="Reservar", var=reservar_var)

    login_cb.grid(row=4, column=1)
    buscar_cb.grid(row=5, column=1)
    reservar_cb.grid(row=6, column=1)

    # Configuración de estilo
    style = ttk.Style()
    style.configure("White.TButton", font=('Helvetica', 10), background='black')
    style.map("White.TButton",
              foreground=[('!active', 'white'), ('active', 'black')],
              background=[('active', 'white')])

    # Crear un botón
    # start_apache = ttk.Button(w, text="Iniciar Apache & Mysql", command=start_xampp, style="TButton")
    # start_apache.grid(row=2, column=0, sticky='w')

    t_login = ttk.Button(w, text="TEST - Login", command=test_login, style="TButton")
    t_login.grid(row=4, column=0, sticky='w')  # Alineación a la izquierda

    t_buscar = ttk.Button(w, text="TEST - Buscar libros", command=test_buscar_libros, style="TButton")
    t_buscar.grid(row=5, column=0, sticky='w')  # Alineación a la izquierda

    t_reservar = ttk.Button(w, text="TEST - Reservar libros", command=test_reservar, style="TButton")
    t_reservar.grid(row=6, column=0, sticky='w')  # Alineación a la izquierda

    status = ttk.Label(w, text="Estado tests: ")
    # Botón para guardar el estado de los CheckBoxes
    guardar_btn = ttk.Button(w, text="Guardar Estado",
                             command=lambda: guardar_estado(login_var, buscar_var, reservar_var))
    guardar_btn.grid(row=8, column=0, sticky='e')

    status.grid(row=9, column=0, sticky='w')
    start_xampp()  # Inicializamos más tarde para no llamar antes al label que su creación

    w.mainloop()


def guardar_estado(login_var, buscar_var, reservar_var):
    with open("resultados.txt", "w") as file:
        file.write(f"Login: {login_var.get()}\n")
        file.write(f"Buscar: {buscar_var.get()}\n")
        file.write(f"Reservar: {reservar_var.get()}\n")
    print("Estado guardado en resultados.txt")


def s(tiempo):
    time.sleep(tiempo)


def launch_menu():
    s(0.5)
    # Es necesario encontrarnos en ./index.php
    pyautogui.moveTo(100, 100)
    pyautogui.click()


if __name__ == '__main__':
    app()
