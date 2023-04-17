# 👋 Python for Education 👋

#### 👨‍💻👩‍💻 Proyecto desarrollado por 👨‍💻👩‍💻
* [Alejandro Castro Martínez](https://github.com/kstro96)
* [Janet Chen He](https://github.com/XingYi98)
* [María José Niño Rodríguez](https://github.com/mjninor99)

* [Juan Diego Sierra Cifuentes](https://github.com/juandisierra10)

#### 👨‍🏫👩‍🏫 Bajo la dirección de 👨‍🏫👩‍🏫 
* Ing. MsC. Martha Cano Morales
* Ing. MsC. PhD. Jairo Alberto Hurtado
* Ing. MsC. PhD. Eduardo Mejía Rodríguez

<img src="https://github.com/Hardware-For-Education/.github-private/blob/main/profile/images/scratch4education-small.png" width="200" />

## 🙋‍♀️ Descripción 🙋‍♀️

Proyecto enfocado en el desarrollo de una plataforma hardware que interactúe con el entorno de programación visual Scratch® a través de sensores y elementos de salida, con fines educativos tecnológicos. 

Específicamente este proyecto está enfocado en el código que se ejecuta en el computador que tiene como objetivo ser el intermediario entre el Scratch® modificado y el Arduino UNO, traduciendo los mensajes enviados por este a mensajes del protocolo Firmata para ser intrepetados por el programa de Arduino.

Proyecto desarrollado en el marco del trabajo de grado como un requisito para optar por el título de ingenier@ electrónic@ de la Pontificia Universidad Javeriana, Bogotá, Colombia en el año 2022 por parte de los integrantes del grupo resaltados anteriormente. 

### 💻 Estructura del repositorio 💻

*Proyecto basado en el desarrollo realizado por [Alan Yoriks](https://github.com/MrYsLabv) en la serie de publicaciones realizadas en su blog [Bots in pieces](https://mryslab.github.io/bots-in-pieces/) bajo el nombre de [Creating a Scratch3 Extension For GPIO Control](https://mryslab.github.io/bots-in-pieces/posts/) en varias partes.*

  * *[Creating a Scratch3 Extension For GPIO Control - Part 1](https://mryslab.github.io/bots-in-pieces/scratch3/gpio/2019/09/15/scratch3-1.html)*
  * *[Creating a Scratch3 Extension For GPIO Control - Part 2 ](https://mryslab.github.io/bots-in-pieces/scratch3/gpio/2019/09/16/scratch3-2.html)*
  * *[Creating a Scratch3 Extension For GPIO Control - Part 3](https://mryslab.github.io/bots-in-pieces/scratch3/gpio/2019/10/03/scratch3-3.html)*
  * *[Creating a Scratch3 Extension For GPIO Control - Part 4](https://mryslab.github.io/bots-in-pieces/scratch3/gpio/2019/10/17/scratch-3-4.html)*
  * *[Scratch 3 Extensions - Part 5 ](https://mryslab.github.io/bots-in-pieces/scratch3/picoboard/circuit-playground-express/2020/02/02/scratch3-5.html)*

El repositorio contiene los distintos archivos desarrollados en Python para realizar la conexion entre el Scratch® modificado y el programa de Arduino. Los archivos principales se encuentran en la carpeta _python_for_education_ fuera de esta carpeta se encuentran los archivos relacionados con la interfaz grafica (imagenes y codigo) y los archivos de licencia correspondiente. 

Dentro de la carpeta _python_for_education_ se encuentran los archivos correspondientes a la ejecucion de este programa:
* El archivo _s3a.py_ es el programa principal. 
* El archivo _install.py_ es un script para la instalacion de las librerias requeridas para la ejecucion del programa principal.
* El archivo _websocket.py_ es aquel programa que crea la conexion entre el Scratch® modificado y el programa de Python. 
* El archivo _backplane.py_ es aquel archivo que sirve de interconexion entre el WebSocket y el Arduino Gateway.
* El archivo _gateway_base_aio.py_ es aquel archivo que lleva dentro las funciones que debe ejecutar cada gateway para cada dispositivo de conexion. 
* El archivo _arduino_gateway.py_ es aquel que define las funciones propuestas en el archivo _gateway_base_aio.py_ para el caso del Arduino. 
* La carpeta _pymata_express_H4E_ contiene distintos modulos que definen constantes y estructuras comunes para los demas programas. 

La carpeta _images_ contiene las imagenes requeridas en este y los demas archivos de explicacion de este repositorio. 

### ⚒ Funcionamiento ⚒

En la siguiente imagen se presenta una breve explicacion grafica de como los distintos archivos descritos anteriormente se ejecutan para cumplir la funcion de interconectar el Scratch® modificado y el programa de Arduino. 

<img src="https://github.com/Hardware-For-Education/Python_For_Education/blob/main/images/Programas.png"/>

Como bien se puede observar anteriormente, el Scratch® modificado envia sus mensajes a traves del programa _websocket.py_ hacia el _backplane.py_ este direcciona la comunicacion hacia el gateway correspondiente, en este caso el gateway es el programa _arduino_gateway.py_. Este ya es el punto que envia los mensajes al programa de Arduino a traves del protocolo Firmata. 

Ahora bien, la ejecucion de este proyecto ocurre desde el archivo _interfaz.py_ y este a su vez ejecuta el archivo _s3a.py_. Este dentro de su ejecucion llama los programas _backplane.py_, _websocket.py_ y _arduino_gateway.py_. La siguiente imagen presenta este comportamiento de ejecucion.  

<img src="https://github.com/Hardware-For-Education/Python_For_Education/blob/main/images/python_execution.png" />

#### ⚒ Funcionamiento interno ⚒

en la carpeta _notes_ se encuentran distintos archivos de informacion con respecto al funcionamiento y ejecucion de los distintos archivos principales de este proyecto. 

* En el archivo [funcionamiento_s3a.md](https://github.com/Hardware-For-Education/Python_For_Education/blob/main/notes/funcionamiento_s3a.md) se puede encontrar mayor informacion con respecto al funcionamiento interno del archivo correspondiente y que modificaciones se pueden realizar.
* En el archivo [funcionamiento_websocket.md](https://github.com/Hardware-For-Education/Python_For_Education/blob/main/notes/funcionamiento_websocket.md) se puede encontrar mayor informacion con respecto al funcionamiento interno del archivo correspondiente y que modificaciones se pueden realizar.
* En el archivo [funcionamiento_backplane.md](https://github.com/Hardware-For-Education/Python_For_Education/blob/main/notes/funcionamiento_backplane.md) se puede encontrar mayor informacion con respecto al funcionamiento interno del archivo correspondiente y que modificaciones se pueden realizar. 
* En el archivo [funcionamiento_arduino_gateway.md](https://github.com/Hardware-For-Education/Python_For_Education/blob/main/notes/funcionamiento_arduino_gateway.md) se puede encontrar mayor informacion con respecto al funcionamiento interno del archivo correspondiente y que modificaciones se pueden realizar.

#### 💿 Creacion ejecutable 💿

Un aspecto importante de este proyecto es la creacion del ejecutable de todo el proyecto. Para esto se realizo una guia que se puede encontrar en el archivo [crear_ejecutable.md](https://github.com/Hardware-For-Education/Python_For_Education/blob/main/notes/crear_ejecutable.md)

#### 📚 Información relevante 📚

Se puede encontrar mayor información con respecto al desarrollo de la extensión OneGPIO desarrollada para Arduino por Alan Yorinks en 

* [Scratch 3 OneGPIO Extensions](https://mryslab.github.io/s3-extend/) Especificamente en la seccion _Preparing Your Computer_ donde se detalla la instalacion de Python y del paquete S3-extend que es el proyecto desarrollado por [Alan Yoriks](https://github.com/MrYsLabv) 
   * Cabe resaltar que este paquete que se instala en este tutorial no contiene las mismas funcionales presentes en este proyecto. Para instalar este proyecto, los pasos se encuentran detallados en [⚠ Puesta en marcha ⚠](https://github.com/Hardware-For-Education/.github-private/blob/main/profile/README.md#-puesta-en-marcha-)
