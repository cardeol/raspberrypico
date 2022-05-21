from machine import Pin, I2C, PWM
from ssd1306 import SSD1306_I2C
from veml7700 import VEML7700
import utime

buzzer = PWM(Pin(15))
pin_sda = 16
pin_sck = 17
limit_sec = 10
light_limit = 25
oled_on = False

oled = None
if oled_on:
    i2c_oled =I2C(0,sda=Pin(pin_sda), scl=Pin(pin_sck), freq=400000)
    oled = SSD1306_I2C(128, 64, i2c_oled)


i2c_veml = I2C(0, sda=Pin(pin_sda), scl=Pin(pin_sck), freq=10000)

veml = VEML7700(address=0x10, i2c=i2c_veml, it=100, gain=1/8)

last_str = ""
playing = False
elapsed = utime.time()

def display(text):
    if not oled_on:
        return
    global last_str
    if last_str == text:
        return
    oled.fill(0)
    oled.text(text, 10, 5)
    oled.show()


def beep():
    # 1568
    global playing
    if playing:
        return
    playing = True
    for i in range(10):
        freq = 1568
        buzzer.duty_u16(4000 * i)
        buzzer.freq(freq + (i*100))
        utime.sleep_ms(50)
        buzzer.duty_u16(0)
        utime.sleep_ms(50)
    playing = False

while True: 
    utime.sleep_ms(500)
    lux_val = veml.read_lux()
    print(lux_val)
    
    if lux_val > light_limit:
        display(str(lux_val) + ' - Alarm')
        t = utime.time()
        if (utime.time() - elapsed) > limit_sec:
            beep()
    else:
        elapsed = utime.time()
        display(str(lux_val))


