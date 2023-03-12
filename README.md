# HC-SR04
Sin librerías extra, llegas lo conectas, lo corres y listo

En la universidad me pidieron hacer un medidor de volumen mediante un HC-SR04 y al momento de buscar informacion
encontre mucha basura, y mediante un poco de estudio logre conectarlo por mi cuenta sin dañar mi microcontrolador

En mi caso use el raspberry pi pico

El HC-SR04 trabaja con voltajes de 5v para entrada y salida

Esto quiere decir que lo alimentaremos con el pin VBUS o VSYS
Tambien deveriamos proteger nuestro micro del voltaje pues la pico solo admite votajes de 3.3v por lo que mediante la relacion V = IR
podemos saber cual es la resistencia necesaria de la siguiente manera:

R = I/V

Por el datasheet del HC-SR04 sabemos que trabaja a 15mA y el volaje que regresa es 5V

R = 15mA/5v
R = 220Ohm's

Por lo que el Pin echo debera ser conectado a la pico medianten la resistencia antes calculada
