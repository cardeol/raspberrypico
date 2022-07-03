from machine import Pin
from time import sleep

motion = False
led = Pin(25, Pin.OUT)
pir = Pin(0, Pin.IN)

def handle_interrupt(pin):  #Avoid using print() inside isr
  global motion
  global led
  global pir
  print(pir.value())
  if(motion == True):
      return
  motion = True
  led.on()
  sleep(1)
  led.off()
  motion = False
  

# condition = Pin.IRQ_RISING | Pin.IRQ_FALLING
condition = Pin.IRQ_FALLING

pir.irq(trigger = condition, handler = handle_interrupt)

