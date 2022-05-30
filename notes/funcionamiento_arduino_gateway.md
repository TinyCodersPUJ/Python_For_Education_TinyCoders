# 👋 Python for Education 👋 arduino_gateway.py 👋

#### 👨‍💻👩‍💻 Proyecto desarrollado por 👨‍💻👩‍💻
* [Alejandro Castro Martínez](https://github.com/kstro96)
* [Janet Chen He](https://github.com/XingYi98)
* [María José Niño Rodríguez](https://github.com/mjninor99)
#### 👨‍🏫👩‍🏫 Bajo la dirección de 👨‍🏫👩‍🏫 
* Ing. MsC. Martha Cano Morales
* Ing. MsC. PhD. Jairo Alberto Hurtado

<img src="https://github.com/Hardware-For-Education/.github-private/blob/main/profile/images/scratch4education-small.png" width="200" />

## 🙋‍♀️ Descripción 🙋‍♀️

Proyecto enfocado en el desarrollo de una plataforma hardware que interactúe con el entorno de programación visual Scratch® a través de sensores y elementos de salida, con fines educativos tecnológicos. 

Específicamente este proyecto está enfocado en el código que se ejecuta en el computador que tiene como objetivo ser el intermediario entre el Scratch® modificado y el Arduino UNO, traduciendo los mensajes enviados por este a mensajes del protocolo Firmata para ser intrepetados por el programa de Arduino.

Proyecto desarrollado en el marco del trabajo de grado como un requisito para optar por el título de ingenier@ electrónic@ de la Pontificia Universidad Javeriana, Bogotá, Colombia en el año 2022 por parte de los integrantes del grupo resaltados anteriormente. 

## 💻 arduino_gateway.py 💻

arduino_gateway.py es el archivo fuente que correponde a la ejecucion del gateway. En si, su funcion principal es ejecutar un programa de conexion entre el arduino y el backplane. De una forma grafica la conexion entre los programas es de la siguiente forma: 

<img src="https://github.com/Hardware-For-Education/Python_For_Education/blob/main/images/Programas.png"/>

Este archivo fue de creacion principal de [Alan Yoriks](https://github.com/MrYsLabv) en su proyecto [s3-extend](https://github.com/MrYsLab/s3-extend). Este archivo se encuentra en [arduino_gateway.py by Alan Yorinks](https://github.com/MrYsLab/python_banyan/blob/master/projects/OneGPIO/arduino_uno/arduino_gateway.py).

### 🏗 Estructura 🏗

Este archivo trabaja como la traducción de los mensajes enviados por la página web de Scratch modificado a mensajes Firmata. Todo esto se realiza a través de dos procesos. 

El primer paso es la definición de los mensajes posibles que pueden ser enviados por la página web de Scratch. Esta definición se realiza en el archivo [_gateway_base_aio.py_](https://github.com/Hardware-For-Education/Python_For_Education/blob/main/python_for_education/gateway_base_aio.py). 

Este archivo cuenta con una variable denominada _command_dictionary_. Esta variable crea un mappeado entre el mensaje que envía la página web de Scratch y la función a ejecutar cuando dicho mensaje sea recibido. un ejemplo de esto es: 

```python
  self.command_dictionary = {'analog_write': self.analog_write}
```

Este ejemplo identifica que cuando se envíe el mensaje 'analog_write', se ejecutará la función _analog_write_. Si bien esta función debe definirse en este mismo archivo también se deben definir en este archivo (_arduino_gateway.py_). La única diferencia es que en el primero solo se encuentra un _raise_ de un error, mientras que en el otro archivo ya se encuentra definida lo pasos de ejecución. 

```python
  async def analog_write(self, topic, payload):
        """
        This method will pass any messages not handled by this class to the
        specific gateway class. Must be overwritten by the hardware gateway class.

        :param topic: message topic

        :param payload: message payload
        """
        raise NotImplementedError
```

Si se desea crear una funcionalidad se requiere esta función con los mismos parámetros (self, topic, payload). 

En el estado actual de la aplicación, las funciones posibles para ejecutar son: 

```python
  'analog_write': self.analog_write,
  'digital_write': self.digital_write,
  'disable_analog_reporting': self.disable_analog_reporting,
  'disable_digital_reporting': self.disable_digital_reporting,
  'enable_analog_reporting': self.disable_analog_reporting,
  'enable_digital_reporting': self.disable_digital_reporting,
  'i2c_read': self.i2c_read,
  'i2c_write': self.i2c_write,
  'play_tone': self.play_tone,
  'pwm_write': self.pwm_write,
  'servo_position': self.servo_position,
  'set_mode_analog_input': self.set_mode_analog_input,
  'set_mode_digital_input': self.set_mode_digital_input,
  'set_mode_digital_input_pullup': self.set_mode_digital_input_pullup,
  'set_mode_digital_output': self.set_mode_digital_output,
  'set_mode_i2c': self.set_mode_i2c,
  'set_mode_pwm': self.set_mode_pwm,
  'set_mode_servo': self.set_mode_servo,
  'set_mode_sonar': self.set_mode_sonar,
  'set_mode_stepper': self.set_mode_stepper,
  'set_mode_tone': self.set_mode_tone,
  'stepper_write': self.stepper_write,
  'set_led_rgb' : self.set_led_rgb,
  'led_rgb' : self.led_rgb,
  'lcd': self.lcd,
  'clear_lcd': self.clear_lcd,
  'circle_lcd': self.circle_lcd,
  'rectangle_lcd': self.rectangle_lcd,
  'triangle_lcd': self.triangle_lcd
```

Una vez definida esta función, se recurre al archivo _arduino_gateway.py_ donde ahora se deben definir los pasos a seguir para cada una de estas funciones. Esta función definida en este archivo tiene como objetivo desglosar los argumentos enviados en el comando para realizar el llamado a otra función en el archivo _pymata_express.py_. 

Un ejemplo de esto es: 

```python
async def digital_write(self, topic, payload):
  """
  This method performs a digital write
  :param topic: message topic
  :param payload: {"command": "digital_write", "pin": “PIN”, "value": “VALUE”}
  """
  await self.arduino.digital_write(payload["pin"], payload['value'])
```

Esta nueva función que se llama a ejecutar está en el archivo _pymata_express.py_. Esta función tranforma los valores recibidos para ser enviados a través del protocolo Firmata. Un ejemplo de ello se encuentra en la función: 

```python
async def digital_write(self, pin, value):
  """
  Set the specified pin to the specified value.

  :param pin: arduino pin number

  :param value: pin value (1 or 0)

  """
  # The command value is not a fixed value, but needs to be calculated
  # using the pin's port number
  port = pin // 8

  calculated_command = PrivateConstants.DIGITAL_MESSAGE + port
  mask = 1 << (pin % 8)
  # Calculate the value for the pin's position in the port mask
  if value == 1:
      PrivateConstants.DIGITAL_OUTPUT_PORT_PINS[port] |= mask
  else:
      PrivateConstants.DIGITAL_OUTPUT_PORT_PINS[port] &= ~mask

  # Assemble the command
  command = (calculated_command,
             PrivateConstants.DIGITAL_OUTPUT_PORT_PINS[port] & 0x7f,
             (PrivateConstants.DIGITAL_OUTPUT_PORT_PINS[port] >> 7)
             & 0x7f)

  await self._send_command(command)
```

Esta función es un ejemplo. De esta cabe resaltar la función _send_command_ que es una función para enviar comandos simples al microcontrolador, y también resaltar que comando se calcula a partir de operaciones de bits. La definición de los mensajes posibles se encuentran en [Definicion protocolo](https://github.com/firmata/protocol/blob/master/protocol.md)

#### ⚒ Demas programas ⚒

* En el archivo [funcionamiento_websocket.md](https://github.com/Hardware-For-Education/Python_For_Education/blob/main/notes/funcionamiento_websocket.md) se puede encontrar mayor informacion con respecto al funcionamiento interno del archivo correspondiente y que modificaciones se pueden realizar.
* En el archivo [funcionamiento_backplane.md](https://github.com/Hardware-For-Education/Python_For_Education/blob/main/notes/funcionamiento_backplane.md) se puede encontrar mayor informacion con respecto al funcionamiento interno del archivo correspondiente y que modificaciones se pueden realizar. 
* En el archivo [funcionamiento_arduino_gateway.md](https://github.com/Hardware-For-Education/Python_For_Education/blob/main/notes/funcionamiento_arduino_gateway.md) se puede encontrar mayor informacion con respecto al funcionamiento interno del archivo correspondiente y que modificaciones se pueden realizar.

#### 💿 Creacion ejecutable 💿

Un aspecto importante de este proyecto es la creacion del ejecutable de todo el proyecto. Para esto se realizo una guia que se puede encontrar en el archivo [crear_ejecutable.md](https://github.com/Hardware-For-Education/Python_For_Education/blob/main/notes/crear_ejecutable.md)

#### 📚 Información relevante 📚

Se puede encontrar mayor información con respecto al desarrollo de la extensión OneGPIO desarrollada para Arduino por Alan Yorinks en 

* [Scratch 3 OneGPIO Extensions](https://mryslab.github.io/s3-extend/) Especificamente en la seccion _Preparing Your Computer_ donde se detalla la instalacion de Python y del paquete S3-extend que es el proyecto desarrollado por [Alan Yoriks](https://github.com/MrYsLabv) 
   * Cabe resaltar que este paquete que se instala en este tutorial no contiene las mismas funcionales presentes en este proyecto. Para instalar este proyecto, los pasos se encuentran detallados en [⚠ Puesta en marcha ⚠](https://github.com/Hardware-For-Education/.github-private/blob/main/profile/README.md#-puesta-en-marcha-)
