import random
import subprocess
import time
import pyautogui
import webbrowser
import tkinter as tk

# v0.2 - Tests OK


def test_login():
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


def test_buscar_libros():
    random.seed(time.time())
    ruta_diblio = r"http://localhost/bibliodigital/"
    libros = ["Viaje al centro de la Tierra", "Los tres cerditos", "Les tres bessones", "El libro de la selva"]

    webbrowser.open(ruta_diblio)
    s(0.5)

    pyautogui.moveTo(150, 200)
    pyautogui.click()  # Cerca
    s(0.5)

    r = random.choice(libros)
    pyautogui.write(r)
    s(0.5)

    pyautogui.moveTo()


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
    random.seed(time.time())
    libros = ["Viaje al centro de la Tierra", "Los tres cerditos", "Les tres bessones", "El libro de la selva"]
    ruta_diblio = r"http://localhost/bibliodigital/reservas.php?libro="

    webbrowser.open(ruta_diblio + random.choice(libros))
    s(0.5)

    pyautogui.moveTo(130, 250)
    pyautogui.click()
    rand_date()
    s(0.5)

    pyautogui.moveTo(120, 280)
    pyautogui.click()
    rand_date()

    pyautogui.moveTo(100, 320)
    pyautogui.click() # Botón reserva


def start_xampp():
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
    """
    Con esto podremos runnear apache y mysql sin entrar a la GUI
    de xampp.
    """


def app():
    print("[MAIN] App iniciada.")

    w = tk.Tk()
    w.title("Tests de caja negra - diblio")
    w.geometry("400x300")
    w.resizable(width=False, height=False)

    intro = tk.Label(w, text="Selecciona un test para ejecutarlo individualmente.")
    intro.grid(row=1, column=0, sticky='w')  # 'w' para alinear a la izquierda (west)

    start_apache = tk.Button(w, text="Iniciar Apache & Mysql", command=start_xampp)
    start_apache.grid(row=2, column=0, sticky='w')  # Alineación a la izquierda

    # Aplicando estilos al botón
    start_apache.config(font=('Helvetica', 10), bg='black', fg='white')

    t_login = tk.Button(w, text="TEST - Login", command=test_login)
    t_login.grid(row=3, column=0, sticky='w')  # Alineación a la izquierda

    t_buscar = tk.Button(w, text="TEST - Buscar libros", command=test_buscar_libros)
    t_buscar.grid(row=4, column=0, sticky='w')  # Alineación a la izquierda

    t_reservar = tk.Button(w, text="TEST - Reservar libros", command=test_reservar)
    t_reservar.grid(row=5, column=0, sticky='w')  # Alineación a la izquierda



    # Con esto la app se seguirá ejecutando de forma indefinida.
    w.mainloop()


def s(tiempo):
    time.sleep(tiempo)


def launch_menu():
    s(0.5)
    # Es necesario encontrarnos en ./index.php
    pyautogui.moveTo(100, 100)
    pyautogui.click()


if __name__ == '__main__':
    app()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
