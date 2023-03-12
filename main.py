#Ultrasonico HC-SR04 by Calak de Astora

from machine import Pin #Importa la libreria I2c y Pin para control de los objetos I2C y los pines GIPO
import utime #Libreria de tiempo

trig = Pin(15, Pin.OUT) #Declara el pin del gatillo en salida
echo = Pin(14, Pin.IN) #Declara el pin del receptor en entrada, NOTA usar resistencia de 220ohm pa no quemar el pico
d = 0 #Delcara una variable distancia y la inicializamos en 0
v = 0.0343 #Declraramos la velocidad en cm/s
 
while True: #Incia ciclo sin fin

    trig.value(1) #Manda el voltaje al gatillo
    utime.sleep(0.00001) #Espera un microsegundo
    trig.value(0) #Apgaga la señal del gatillo

    while echo.value() == 0: #Inicia bucle mientras que el receptor no reciba nada
        init = utime.ticks_us() #Declrara una variable que almacena el tiempo de ida
    #Fin del bucle

    while echo.value() == 1: #Inicia un bucle mientras que el receptor regrese valores
        fin = utime.ticks_us() #Declara una variable que almacena el tiempo de vuelta
    #Fin del bucle

    t = fin - init #Calcula el tiempo
    d = (t * v) / 2 #Calcula distancia
    
    print("Distancia es: " + str(d) + "cm") #Imprime distancia
    
    utime.sleep(3) #Pausa el programa 3 segundos

#Fin del programa
