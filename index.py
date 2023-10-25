'''
from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(2))
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v


#ADC.ATTN_0DB: Maximum voltage of 1.2V
#ADC.ATTN_2_5DB: Maximum voltage of 1.5V
#ADC.ATTN_6DB: Maximum voltage of 2.0V
#ADC.ATTN_11DB: Maximum voltage of 3.3V


while True:
  pot_value = pot.read()
  print(pot_value)
  sleep(0.1)
'''
import machine, time
a = machine.ADC(machine.Pin(32))
while True:
    sample = a.read()  # we want 16 bits, a.read() returns 10 bits
    print(sample)
    time.sleep(1/44100)
