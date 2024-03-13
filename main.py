import machine
from machine import Pin, I2C
from utime import sleep_ms
from vl53l0x import VL53L0X

i2c = I2C(id = 0, scl = 1, sda = 0)

senzor1 = VL53L0X(i2c)

while True:
    print(senzor1.ping()-20, "mm")
    sleep_ms(500)