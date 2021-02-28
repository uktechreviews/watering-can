import ssd1306
import machine
import time
import uos
import machine
from machine import ADC, Pin
    

print(uos.uname())
print("Freq: "  + str(machine.freq()) + " Hz")
print("128x64 SSD1306 I2C OLED on Raspberry Pi Pico")

WIDTH = 128
HEIGHT = 32

i2c = machine.I2C(0)

print("Available i2c devices: "+ str(i2c.scan()))
oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.fill(0)

def line(l):
    oled.text("x", l, 0)
    oled.text("x", l,5)
    oled.text("x", l,10)
    oled.text("x", l,15)
    oled.text("x", l,20)
    oled.text("x", l,25)

def read_sensor():
    adc = ADC(Pin(26))
    sensor = adc.read_u16()
    return sensor
    

while True:
    value = read_sensor()
    scaled = ((value-20500)/3000)
    moisture = int(15-scaled)
    print ("moisture value " + str(moisture))
    l = 0
    while l <= moisture*10:
        line(l)
        oled.show()
        time.sleep(0.2)
        l+=10
    oled.fill(0)
    time.sleep(1)