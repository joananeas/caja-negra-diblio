![Static Badge](https://img.shields.io/badge/diblio-testing-4A68A0?style=flat)
![Static Badge](https://img.shields.io/badge/bibliodigital-testing-4A68A0?style=flat)

# Black Box Testing @diblio
**SOLO PARA WINDOWS -** Abre una ventana de 400*400 con varios botones. 
Permite automatizar el testeo de mi repositorio bibliodigital/diblio.
Utiliza pyautogui, y solo permite el testeo de la UI, aunque hace peticiones a la API de forma indirecta,
por ejemplo: login, búsqueda de libros o empezar una reserva.

Se mueve por píxeles, por lo que no he comprobado aún, pero puede que en pantallas con resoluciones distintas
se comporte de forma distinta, mi entorno es de escritorio, **1920*1080px**.

Es **necesario** tener instalado XAMPP, en la ruta ```C:\xampp```.  
También hay que clonar el repo ```https://github.com/joananeas/bibliodigital.git``` en ```C:\xampp\htdocs```.  
El script accede por la url a ```http://localhost/bibliodigital``` (puerto 80, obviamente).  

***Obligatorio*** crear una BBDD llamada bibliodigital y subir el bibliodigital-min.sql o
realizar la instalación de bibliodigital.

### Descarga el [exe](https://drive.google.com/file/d/1QKNzTuwvJwRHhgTTFLs5EkcFl6GgHFHX/view?usp=sharing).

