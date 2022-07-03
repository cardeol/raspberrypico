from machine import Pin
from time import sleep

motion = False
led = Pin(25, Pin.OUT)
pir = Pin(0, Pin.IN)

def handle_interrupt(pin):  #Avoid using print() inside isr
  global motion
  global led
  global pir
  print("2")
  print(pir.value())
  if(motion == True):
      return
  motion = True
  led.on()
  print("motion detected")
  sleep(3)
  led.off()
  print("pin off")
  motion = False
  

pir.irq(trigger = Pin.IRQ_RISING | Pin.IRQ_FALLING, handler = handle_interrupt)

