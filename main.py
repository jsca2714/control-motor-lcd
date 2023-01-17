import pygame
from pynput import keyboard
import I2C_LCD_driver
from gpiozero import LED, Button, Motor
from signal import pause
import sys
import RPi.GPIO as GPIO
import time
from time import sleep
from pynput import keyboard as kb

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_OFF)
mylcd = I2C_LCD_driver.lcd()
pygame.init()
window = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Pygame Demonstration")

# Variables globales

# y declaracion de pines

velocidad = 1

x = 1
motor = Motor(26, 19)
btn3 = Button(13)
posicion = 0

def menuprin1():
    mylcd.lcd_clear()
    mylcd.lcd_display_string('------PWM------*')
    mylcd.lcd_display_string('----SENTIDO-----', 2)
    sleep(0.25)

def menuprin2():
    mylcd.lcd_clear()
    mylcd.lcd_display_string('------PWM-------')
    mylcd.lcd_display_string('----SENTIDO----*', 2)

def menuprin3():
    mylcd.lcd_clear()
    mylcd.lcd_display_string('----SENTIDO-----')
    mylcd.lcd_display_string('---VUELTAS-----*', 2)

def menu1():
    mylcd.lcd_clear()
    mylcd.lcd_display_string('velocidad')
    mylcd.lcd_display_string('%', 2)

def menu2():
    mylcd.lcd_clear()
    mylcd.lcd_display_string('direccion')
    mylcd.lcd_display_string('1=DER , 2=IZQ', 2)

def menu3():
    mylcd.lcd_clear()
    mylcd.lcd_display_string('indique #vueltas')
    mylcd.lcd_display_string('#', 2)

def Motor():
    mylcd.lcd_clear()
    menu1()
    global velocidad
    print("motor")
    velocidad2 = int(input("digite la velocidad:"))
    if velocidad2 == 10 or velocidad2 == 20 or velocidad2 == 30 or velocidad2 == 40 or velocidad2 == 50:
        mylcd.lcd_display_string("" + str(velocidad2), 2, 2)
    if velocidad2 == 10:
        velocidad2 = 18
    if velocidad==20:
        velocidad = 26
        velocidad = velocidad2 * 0.01
    else:
        mylcd.lcd_display_string("error", 2, 3)
        sleep(0.3)

def vueltas(velocidad, x):
    mylcd.lcd_clear()
    menu3()
    count = 0
    vueltas = int(input("digite #vueltas"))
    mylcd.lcd_display_string("" + str(vueltas), 2, 4)
    if x == 1:
        motor.forward(0.7)
        sleep(0.05)
        while vueltas > count:
            motor.forward(velocidad)
            if GPIO.input(17) == 1:
                count += 1
                print(count)
                mylcd.lcd_clear()
                mylcd.lcd_display_string("----#VUELTAS----")
                mylcd.lcd_display_string("" + str(count), 2, 7)
                while GPIO.input(17) == 1:
                    pass
                if btn3.is_pressed:
                    pausa(x)

    if x == 2:
        motor.backward(0.7)
        sleep(0.05)
        while vueltas > count:
            motor.backward(velocidad)
            if GPIO.input(17) == 1:
                count += 1

                print(count)
                mylcd.lcd_clear()
                mylcd.lcd_display_string("----#VUELTAS----")
                mylcd.lcd_display_string("" + str(count), 2, 7)
                while GPIO.input(17) == 1:
                    pass
                if btn3.is_pressed:
                    pausa(x)

    motor.stop()

def sentido_giro(velocidad):
    mylcd.lcd_clear()
    global x
    menu2()
    sentido = int(input("indique la direccion (1(der))(2(izq)):"))
    x = sentido
    mylcd.lcd_display_string("" + str(x), 2, 15)
    sleep(0.5)

def pausa(x):
    mylcd.lcd_clear()
    sleep(0.1)
    motor.stop()
    cont = 20
    while cont > 0:
        cont -= 1
        mylcd.lcd_clear()
        mylcd.lcd_display_string('-----PAUSA------', 1)
        mylcd.lcd_display_string("" + str(cont), 2, 7)
        sleep(1)
        if x == 1:
            motor.forward(0.7)
            sleep(0.06)
        if x==2:
            motor.backward(0.7)
            sleep(0.06)
            
def main_menu():
    global posicion
    flag = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                posicion += 1
            elif event.key == pygame.K_UP:
                posicion -= 1
            
            # check if posicion is -3 or 1 or 4
            if posicion in [-3, 1, 4]:
                menuprin1()
                flag = 1
                if event.key == pygame.K_RETURN:
                    mylcd.lcd_clear()
                    sleep(0.1)
                    Motor()
                    sleep(1)
                    menuprin1()
                    flag = 0
            
            # check if posicion is -2 or 2 or 5
            elif posicion in [-2, 2, 5]:
                menuprin2()
                flag = 1
                if event.key == pygame.K_RETURN:
                    mylcd.lcd_clear()
                    sleep(0.1)
                    sentido_giro(velocidad)
                    sleep(1)
                    menuprin2()
                    flag = 0
            
            # check if posicion is -1 or 3 or 6
            elif posicion in [-1, 3, 6]:
                menuprin3()
                flag = 1
                if event.key == pygame.K_RETURN:
                    mylcd.lcd_clear()
                    sleep(0.1)
                    vueltas(velocidad,x)
                    sleep(1)
                    menuprin3()
                    flag = 0
            
            elif posicion == 0:
                pass

while True:
    main_menu()
    pygame.quit()

