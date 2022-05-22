
from machine import Pin, PWM
import utime

class Buzzer:
    def __init__(self, pin_number):
        # config
        self.buzzer = PWM(Pin(pin_number))
        self.playing = False
        self.freq = 1200
        
    def beep(self):
        for i in range(20):
            self.buzzer.duty_u16(30000)
            self.buzzer.freq(self.freq + (i*100))
            utime.sleep_ms(50)
            self.buzzer.duty_u16(0)
            utime.sleep_ms(50)
        self.playing = False

    def duty_u16(self, params):
        self.buzzer.duty_u16(params)

    def freq(self, freq):
        self.buzzer.freq(freq)

    def sleep_ms(self, t):
        utime.sleep_ms(t)

    def sleep(self, t):
        utime.sleep_ms(t * 1000)