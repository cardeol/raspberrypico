from machine import Pin, Timer
from buzzer import Buzzer
from light_sensor import LightSensor
import utime

timer = Timer()

class SensorControl:  
    def __init__(self):
        # Init
        self.limit_sec = 350
        self.light_limit = 8
        self.buzzer = Buzzer(15)
        self.sensor = LightSensor(16,17)
        self.init_time = utime.time()
        
        # turn on off led
        led = Pin(25, Pin.OUT)
        led.high()
        utime.sleep_ms(300)
        led.low()

    def check(self, *args, **kwargs):
        lux_val = self.sensor.read()

        if lux_val > self.light_limit:
            elapsed = utime.time() - self.init_time
            if elapsed > self.limit_sec:
                self.buzzer.beep()
        else:
            self.init_time = utime.time()

mysensor = SensorControl()

timer.init(freq=1/5, mode=Timer.PERIODIC, callback=mysensor.check)

