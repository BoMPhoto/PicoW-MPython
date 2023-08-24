# File: Pico_LowPassFilter.py. Created on 2023-08-18 by Bo Mathisen.
# Low Pass filtering is using in the Pico & MPU6050 proj.
# 

from machine import Pin, I2C
import math
import time
from time import sleep

from imu import MPU6050

# Verify Pico I2C channel, SDA and SCL GPIO-ports. 
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400_000)

sensor = MPU6050(i2c)  # Test by using MPU6050.
filtered_ax = 0
alpha = 0.85  # must be between 0 and 1 inclusive


def low_pass_filter(prev_value, new_value):
    return alpha * prev_value + (1 - alpha) * new_value


while True:
    ax_new = sensor.accel.x  # make a new reading from I2C-pin
    filtered_ax = low_pass_filter(filtered_ax, ax_new)
    print("filtered_ax: ", filtered_ax, "raw ax", ax_new)
    time.sleep(1/10)
