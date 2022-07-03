from machine import Pin, PWM
from time import sleep

motion = False
led = Pin(25, Pin.OUT)
pir = Pin(0, Pin.IN)
beeper = PWM(Pin(1))

def beep():
    global beeper
    beeper.duty_u16(2500)
    beeper.freq(3500)
    sleep(0.3)
    beeper.duty_u16(0)

def handle_interrupt(pin):  #Avoid using print() inside isr
  global motion
  global led
  global pir
  print(pir.value())
  if(motion == True):
      return
  motion = True
  led.on()
  beep()
  led.off()
  motion = False
  

# condition = Pin.IRQ_RISING | Pin.IRQ_FALLING
condition = Pin.IRQ_FALLING

pir.irq(trigger = condition, handler = handle_interrupt)


