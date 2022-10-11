from machine import Pin
import utime

#led = Pin(25, Pin.OUT)
#led = machine.Pin(25, machine.Pin.OUT)

#while True:
#    led.value(1)
#    utime.sleep(1.0)
#    led.value(0)
#    utime.sleep(1.0)

led1 = Pin(25, Pin.OUT)
#led2 = Pin(28, Pin.OUT)
led1.low()
#led2.low()

while True:
    led1.toggle()
#    led2.toggle()
    print("Toggle")
    utime.sleep(1)

# onboard_led = machine.Pin(15, machine.Pin.OUT)
# #led2 = machine.Pin(15, machine.Pin.OUT)
# button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
# 
# while True:
#     if button.value() == 1:
#         onboard_led.value(1)
# #        led2.value(1)
#         utime.sleep(0.5)
#     else:
#         onboard_led.value(0)
# #    led2.value(0)

