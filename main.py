import subprocess
import time
import pyautogui
import webbrowser

# v0.1 :0

def s(tiempo):
    time.sleep(tiempo)
def prueba():
    ruta_diblio = r"http://localhost/bibliodigital/login.php" # Abre una pestaña con la dirección del proyecto
    xampp = r"C:\xampp\xampp-control" # Ruta absoluta xampp
    #subprocess.Popen(xampp)
    s(1)
    pyautogui.moveTo(410, 145)
    #pyautogui.click() # Click en apache (start)
    s(0.5)
    pyautogui.moveTo(410, 170)
    #pyautogui.click() # Click en apache (start)

    s(0.5)
    webbrowser.open(ruta_diblio) # Abrimos el navegador
    s(1)
    pyautogui.moveTo(880, 520)
    pyautogui.click() # Correo (login), click.
    s(0.5)
    pyautogui.write("joananeas") # user admin.
    s(1)
    pyautogui.moveTo(880, 550)
    pyautogui.click()
    s(1)

if __name__ == '__main__':
    prueba()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
