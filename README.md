# Proyecto de Motor de PWM
Este proyecto utiliza un motor de PWM conectado a un Raspberry Pi para controlar la velocidad y la dirección del motor. El estado del motor se muestra en una pantalla LCD I2C.

## Dependencias
Para ejecutar este código, es necesario tener las siguientes dependencias instaladas:

- pygame
- pynput
- I2C_LCD_driver
- gpiozero
- RPi.GPIO
## Ejecución
1. Conecte su motor de PWM y pantalla LCD I2C al Raspberry Pi según las especificaciones del fabricante.
2. Asegúrese de que las dependencias mencionadas anteriormente estén instaladas en su dispositivo.
3. Ejecute el código en su Raspberry Pi utilizando una herramienta como IDLE o el terminal.
## Explicación del código
- El código inicia importando las bibliotecas necesarias y configurando el modo de los pines del Raspberry Pi.
- La variable global velocidad se utiliza para almacenar la velocidad del motor y se inicializa en 1.
- El pin 26 se utiliza para controlar la velocidad del motor y el pin 19 se utiliza para controlar la dirección del motor. El botón conectado al pin 13 se utiliza para cambiar entre menús en la pantalla LCD.
- La función menuprin1, menuprin2, menuprin3,menu1, menu2 y menu3 son utilizadas para mostrar mensajes en la pantalla LCD.
- La función Motor se utiliza para controlar la velocidad del motor. El usuario es solicitado ingresar una velocidad y si es 10, 20, 30, 40, 50 entonces se muestra en pantalla y se guarda en velocidad, sino muestra un error.
- La función vueltas se utiliza para controlar la dirección y el número de vueltas del motor. El usuario es solicitado ingresar el número de vueltas y el motor gira en la dirección especificada.
- El código utiliza un bucle while para controlar el número de vueltas del motor y utiliza la señal del pin 17 para contar las vueltas.
## Interacción del usuario
El usuario es solicitado ingresar la velocidad del motor y el número de vueltas en el menú correspondiente. También se puede utilizar el botón conectado al pin 13 para cambiar entre menús en la pantalla LCD.

## Notas adicionales
Asegúrese de configurar los pines del Raspberry Pi correctamente antes de ejecutar el código. Si tiene problemas para ejecutar el código, revise la conexión de los componentes y asegúrese de que las dependencias estén instaladas correctamente.
También es recomendable verificar la compatibilidad de los componentes utilizados con el modelo de Raspberry Pi que está utilizando.
Este código es solo un ejemplo básico de cómo controlar un motor de PWM con un Raspberry Pi y puede ser modificado y expandido según las necesidades del proyecto.