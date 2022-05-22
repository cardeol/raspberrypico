
from machine import Pin, I2C
from veml7700 import VEML7700 # light sensor

class LightSensor:   # default 16,17 example
    def __init__(self, sda, sck):
        self.i2c_veml = I2C(0, sda=Pin(sda), scl=Pin(sck), freq=10000)
        self.veml = VEML7700(address=0x10, i2c=self.i2c_veml, it=100, gain=1/8)
        
    def read(self):
        return self.veml.read_lux()
