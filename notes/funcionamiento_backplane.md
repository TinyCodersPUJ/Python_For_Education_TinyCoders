# 👋 Python for Education 👋 backplane.py 👋

#### 👨‍💻👩‍💻 Proyecto desarrollado por 👨‍💻👩‍💻
* [Alejandro Castro Martínez](https://github.com/kstro96)
* [Janet Chen He](https://github.com/XingYi98)
* [María José Niño Rodríguez](https://github.com/mjninor99)
* [Juan Diego Sierra Cifuentes](https://github.com/juandisierra10)
* [Thomas Morales Varón](https://github.com/Thom037)
#### 👨‍🏫👩‍🏫 Bajo la dirección de 👨‍🏫👩‍🏫 
* Ing. MsC. Martha Cano Morales
* Ing. MsC. PhD. Jairo Alberto Hurtado
* Ing. MsC. PhD. Eduardo Mejía Rodríguez
<img src="https://github.com/Hardware-For-Education/.github-private/blob/main/profile/images/scratch4education-small.png" width="200" />

## 🙋‍♀️ Descripción 🙋‍♀️

Proyecto enfocado en el desarrollo de una plataforma hardware que interactúe con el entorno de programación visual Scratch® a través de sensores y elementos de salida, con fines educativos tecnológicos. 

Específicamente este proyecto está enfocado en el código que se ejecuta en el computador que tiene como objetivo ser el intermediario entre el Scratch® modificado y el Arduino UNO, traduciendo los mensajes enviados por este a mensajes del protocolo Firmata para ser intrepetados por el programa de Arduino.

Proyecto desarrollado en el marco del trabajo de grado como un requisito para optar por el título de ingenier@ electrónic@ de la Pontificia Universidad Javeriana, Bogotá, Colombia en el año 2022 por parte de los integrantes del grupo resaltados anteriormente. 

## 💻 backplane.py 💻

backplane.py es el archivo fuente que correponde a la ejecucion del backplane. En si, su funcion principal es ejecutar un programa de conexion entre el websocket y el arduino gateway con la ayuda del framework Python Banyan. De una forma grafica la conexion entre los programas es de la siguiente forma: 

<img src="https://github.com/Hardware-For-Education/Python_For_Education/blob/main/images/Programas.png"/>

Este archivo fue de creacion principal de [Alan Yoriks](https://github.com/MrYsLabv) en su proyecto [s3-extend](https://github.com/MrYsLab/s3-extend). Este archivo se encuentra en [backplane.py by Alan Yorinks](https://github.com/MrYsLab/python_banyan/blob/master/python_banyan/backplane/backplane.py).

### 🏗 Estructura 🏗

Este programa funciona bajo la premisa de conectar los otros dos programas principales. Esta clase instancia un reenviador ZeroMQ que actúa como backplane del software python_banyan. Todos los demás componentes usan una dirección TCP común para conectarse al backplane y reenviar sus mensajes. Consulte [Learning ZMQ](http://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/devices/forwarder.html) para obtener información sobre el reenviador.

Este archivo no sufrió ningún cambio para este proyecto ya que funciona perfectamente. 

#### ⚒ Demas programas ⚒

* En el archivo [funcionamiento_websocket.md](https://github.com/Hardware-For-Education/Python_For_Education/blob/main/notes/funcionamiento_websocket.md) se puede encontrar mayor informacion con respecto al funcionamiento interno del archivo correspondiente y que modificaciones se pueden realizar.
* En el archivo [funcionamiento_s3a.md](https://github.com/Hardware-For-Education/Python_For_Education/blob/main/notes/funcionamiento_s3a.md) se puede encontrar mayor informacion con respecto al funcionamiento interno del archivo correspondiente y que modificaciones se pueden realizar. 
* En el archivo [funcionamiento_arduino_gateway.md](https://github.com/Hardware-For-Education/Python_For_Education/blob/main/notes/funcionamiento_arduino_gateway.md) se puede encontrar mayor informacion con respecto al funcionamiento interno del archivo correspondiente y que modificaciones se pueden realizar.

#### 💿 Creacion ejecutable 💿

Un aspecto importante de este proyecto es la creacion del ejecutable de todo el proyecto. Para esto se realizo una guia que se puede encontrar en el archivo [crear_ejecutable.md](https://github.com/Hardware-For-Education/Python_For_Education/blob/main/notes/crear_ejecutable.md)

#### 📚 Información relevante 📚

Se puede encontrar mayor información con respecto al desarrollo de la extensión OneGPIO desarrollada para Arduino por Alan Yorinks en 

* [Scratch 3 OneGPIO Extensions](https://mryslab.github.io/s3-extend/) Especificamente en la seccion _Preparing Your Computer_ donde se detalla la instalacion de Python y del paquete S3-extend que es el proyecto desarrollado por [Alan Yoriks](https://github.com/MrYsLabv) 
   * Cabe resaltar que este paquete que se instala en este tutorial no contiene las mismas funcionales presentes en este proyecto. Para instalar este proyecto, los pasos se encuentran detallados en [⚠ Puesta en marcha ⚠](https://github.com/Hardware-For-Education/.github-private/blob/main/profile/README.md#-puesta-en-marcha-)
* [Python Banyan User Guide](https://mryslab.github.io/python_banyan/users_guide/) Guia de usuario del framework Python Bayan para el desarrollo de aplicaciones asincrónicas flexibles, sin bloqueos y basadas en eventos. 
* [Python Banyan Code](https://github.com/MrYsLab/python_banyan) Base de codigo del framework Python Banyan desarrollado por [Alan Yoriks](https://github.com/MrYsLabv) 
